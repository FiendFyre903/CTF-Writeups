# import rAnDoM

> I heard python's prng was insecure. HA IMAGINE. imma make it more secure, what ? no, yes it is secure now. pinky swear.

## About the challenge

We got a python encryption script [chall.py](chall.py) that uses a custom [rAnDoM](rAnDoM.py) module and some [output](out.txt). 

The script groups every 4 characters as one chunk and converts it to integers. And each integer is used as a seed for the rAnDoM module and uses a custom gEtRanDBitS function to generate 6 values that are then hexed and printed out. 

```python
from rAnDoM import *
from Crypto.Util.number import *

flag = b"nite{REDACTED}"
chunks = [bytes_to_long(flag[i:i+4]) for i in range(0, len(flag), 4)]

yap = ""
for i in chunks:
    rAnDoM.sEeD(i)
    yap += hex(rAnDoM.gEtRanDBitS(32))
    yap += hex(rAnDoM.gEtRanDBitS(32))
    yap += hex(rAnDoM.gEtRanDBitS(32))
    yap += hex(rAnDoM.gEtRanDBitS(32))
    yap += hex(rAnDoM.gEtRanDBitS(32))
    yap += hex(rAnDoM.gEtRanDBitS(32))

print("WHAT IS BRO YAPPING ?!!")
print(f"\nbro :\n{yap}")
print("\nBRO WHAT ??!?!")
```

The parts of the rAnDoM module that are used is:-

```python
class rAnDoM:
    current_seed = 0
    indexes = [0,1,2,227,228,229]
    index = 0

    def sEeD(cls, seed) -> None:
            if not isinstance(seed, (type(None), int, float, str, bytes, bytearray)):
                raise TypeError('The only supported seed types are: None,\n'
                                'int, float, str, bytes, and bytearray.')
            cls.current_seed = seed
            random.seed(seed)

    def gEtRanDBitS(cls, bits : int) -> int:
            cls.sEeD(cls.current_seed)
            num = [random.getrandbits(32) for _ in range(624)][cls.indexes[cls.index % len(cls.indexes)]]
            cls.index += 1
            return int(bin(num**(bits // 32))[2:bits+2], 2)
```



## How to Solve

We can see that there are 48 hex values in the output. Dividing by 6 we get 8 chunks of data or 8 unique seeds that are used, and since each chunk is 4 characters, that gives us a flag of 32 characters.

Our goal is to find these 8 seeds.

Since each chunk is 4 ASCII characters that have a value of 0-255 which is 256 (2^8) values , the total seed would have a max value of 2^32 or about 4 billion. Using multiprocessing this is not a large range at all. However we know that only characters upto an ASCII value of 125 will actually be used, so we can reduce the possibilities to exactly 2_147_483_648 values which i rounded up to 2_200_000_000 

The way the gEtRanDBitS function works is, it generates an array of 624 values using the input seed and the `random` module and takes 6 integers out of it and converts them to binary and takes the top x bits (in our case 32). We dont have to worry about the truncating since it generates 32 bit values by default anyways. 

Her another optimisation I did was that instead of generating 624 random values for each seed like the gEtRanDBitS function did, I only generated values up to the max index we would be checking (229). 

The [solution](solve.py) took about 30 mins to run and gave me the flag.

```
nite{br0_y4pp1ng_s33d_sl1pp1ng}
```