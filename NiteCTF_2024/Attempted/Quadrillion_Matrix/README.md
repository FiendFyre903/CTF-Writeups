# Quadrillion Matrix

> The matrices ate my flag. Fight 'em.

## About the challenge

We are given a python file and the output.

First the flag is converted to binary 

```python
with open('flag', 'rb') as f:
    flag = bin(bytes_to_long(f.read()))[2:]
```

The python file generates a random prime p 

```python
p = getPrime(256)
```

For each number (0/1) in the binary of the flag(starting from MSB), A 2*2 matrix `M` is created  and appended to a list called `inp` (the matrix creation function (which is unknown) takes p as an argument).

```python
for i in flag:
    M = gen_matrix(p)
    inp.append(list(M))
```

Another matrice is created by taking a power of M and is appended to another list `out`.

```python
# inside the for loop
    out.append( list((M**(random.randrange(3+int(i), p, 2))) * (M**(random.randrange(3, p, 2)))) )
```

We are provided with `p`, `inp` and `out`.

## Approach

Observation -> we dont need to find the power of M, but only whether it is odd or even.

> If its odd -> i is 1 <br>
If its even -> i is 0

1. I first tried a simple algorithm to check if the power is even or odd, checking if the determinant of the matrix in `out` was a perfect square or not. 

```python
from sage.all import *

det_in = [0 for _ in range(len(inp))]
det_out = [0 for _ in range(len(out))]

for i in range(len(inp)):
    m = Matrix(inp[i])
    det_in[i]= m.determinant()

for i in range(len(out)):
    m = Matrix(out[i])
    det_out[i]= m.determinant()

bin_flag = ""

for i in range(len(inp)):
    if(det_in[i]<0):
        if(det_out[i]>0):
            bin_flag[i] = '0'
        else:
            bin_flag[i] = '1'
        
    elif(det_out[i].is_square()):
        bin_flag[i] = '0'
    else:
        bin_flag[i] = '1'

print(''.join(bin_flag))
```

This did not give me a proper result and i figured maybe the number sizes are too long adn due to approximations/flaoting point issues the `is_square` method wasnt working as intended, which was weird since sage is made for large numbers but i couldnt think of any other reason at the moment. So i tried another method.

2. This method was based on the fact that <br>
n^(2*k) % (n+1) = 1  <br>
n^(2*k+1) % (n+1) = n.

    Again, i used the determinants here but it didnt work


The reason that neither method worked was that every value in the matrix was in a field p.
This messed up the approach.

I couldnt find a way to make it work for field p.

