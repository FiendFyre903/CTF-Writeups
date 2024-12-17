import random
import numpy as np
from multiprocessing import Pool, Value, Lock
import time
import ctypes

# Convert to numpy arrays for faster comparison
hex_chunks = np.array([
    [0xef6ff40f, 0x8b18b98a, 0x9d0bbac8, 0x6fb7ef77, 0x2d951fc5, 0xff8a2516],
    [0xbbfdc204, 0xf220f9b1, 0x5719a00d, 0xb1282eb9, 0xd2f998d0, 0xf69dbed5],
    [0xcf060ec4, 0x5927208f, 0x7d61ee43, 0xfde565e3, 0xf5b8ff5e, 0x3768f0dd],
    [0x6ded6f68, 0x58a5ec3c, 0xa5f018b8, 0xcaba6cf5, 0xd56d9fd0, 0x8d174687],
    [0x572e5fa9, 0x93c6c27d, 0xede60bca, 0xb554453b, 0x83211af8, 0x35d53b58],
    [0x1d31f12e, 0x89b9ad36, 0x81ace1c0, 0x36dadebd, 0x146f624e, 0x4c10e926],
    [0xa3a2e4d6, 0x728e18c9, 0xb301ce5a, 0x283fc702, 0x310bcd90, 0x833c81f8],
    [0x23420e2a, 0x6af59eaf, 0xb2cc8a75, 0x97512aef, 0x8a5b383f, 0x0f0c0a4b]
], dtype=np.uint32)

indexes = np.array([0, 1, 2, 227, 228, 229])

# Shared counter for progress tracking
counter = Value(ctypes.c_ulonglong, 0)
counter_lock = Lock()

def process_seeds(args):    
    start, end, chunk_size = args
    local_chunks = np.zeros(8, dtype=np.uint64)
    local_counter = 0
    
    # Pre-allocate the array for random numbers
    num_arr = np.zeros(max(indexes) + 1, dtype=np.uint32)
    
    for seed in range(start, end):
        local_counter += 1
        if local_counter >= chunk_size:
            with counter_lock:
                counter.value += local_counter
            local_counter = 0
            print(f"Processed {counter.value:,} seeds")
        
        random.seed(seed)
        
        # Generate only the numbers we need
        for i in range(230):
            num_arr[i] = random.getrandbits(32)
        
        # Extract only the needed numbers using fancy indexing
        extracted_numbers = num_arr[indexes]
        
        # Check each chunk using vectorized operations
        for chunk_idx, chunk in enumerate(hex_chunks):
            if np.array_equal(extracted_numbers, chunk):
                print(f"\nFound match for chunk {chunk_idx} with seed {seed}")
                local_chunks[chunk_idx] = seed
                
                # Early exit if this chunk was found
                break
    
    # Add any remaining count
    with counter_lock:
        counter.value += local_counter
        
    return local_chunks

def main():
    start_time = time.time()
    
    # Configuration
    num_processes = 12  
    start_seed = 0 #allows to stop the program and restart later and avoid searhcing the same seeds again.
    total_seeds = 2_200_000_000
    chunk_size = 1_000_000  # Report progress every million seeds (Because I needed to see how long it will take)
    
    # Calculate ranges for each process
    process_chunk_size = total_seeds // num_processes
    ranges = [(i * process_chunk_size + start_seed, 
              min((i + 1) * process_chunk_size, total_seeds),
              chunk_size) 
             for i in range(num_processes)]
    print(ranges)
    
    # Create pool and run processes
    with Pool(processes=num_processes) as pool:
        results = pool.map(process_seeds, ranges)
    
    # Combine results
    final_chunks = np.zeros(8, dtype=np.uint64)
    for result in results:
        mask = result != 0
        final_chunks[mask] = result[mask]
    
    # Print final results
    print("\nSearch completed!")
    print(f"Total seeds processed: {counter.value:,}")
    print(f"Total time: {time.time() - start_time:.2f} seconds")
    print("\nResults:")
    for i, seed in enumerate(final_chunks):
        if seed != 0:
            print(f"Chunk {i}: Seed {seed}")
        else:
            print(f"Chunk {i}: Not found")

if __name__ == "__main__":
    main()
