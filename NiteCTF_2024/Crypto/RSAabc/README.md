# RSAabc

> A blend of encryption methods hides the answer. You might flip out a bit but don't worry, can you crack the code?

## About the challenge

The description mentions a blend of encryptions meaning its possible that more than one encryption is used, either in series or for different parts.

We are provided with the [encryption script](chal/cipher.py) and the [output](chal/out.txt).

The output has 3 parts
A cypher of the flag  - `mrgπeτfΟΔςoΝeηiδyegsλexlwVαehιΠπμZe` <br>
An array of integers named `ct` <br>
An array of integers named `n`

# How to Solve

The cipher `mrgπeτfΟΔςoΝeηiδyegsλexlwVαehιΠπμZe` contains both english and greek characters, both have a different encryption process and hence need to be deciphered in a different manner.

e's represent special characters that we can insert by observation.

For the non-greek characters(There are some non-greek characters in the dictionary as well, we will decipher those the same way as other greek characters.), we can just invert the characterss using the following table that works both ways.

ABCDEFGHIJKLM
ZYXWVUTSRQPON

In which A becomes Z and vice versa. (identical for lower case)

We get `nit?{?u???lY_?r?b_th?_s????A}`


For the greek characters :-

Using the substitution table in the encrypt script, we can convert them to their corresponding english letters. 

The googly function uses XOR for one bit based on the ASCII value of the english letter and the reverse of XOR is just XORing it again , so we can use the googly function as is. (Googly is used on the greek character)

Then we can perform RSA using the given n value on the Greek character (after using googly.)

For RSA I found the factors of n using (https://factordb.com) and plugged the p and q values in the following script

```python
from Crypto.Util.number import *
n = smth
p = smth
q = smth
ct = smth
e = 65537
phi = (p-1)*(q-1)
d = pow(e,-1,phi)
pt = pow(ct,d,n)
print(int_to_string(pt))

```

Doing this process for each character gives us the flag 

```
nite{quICklY_grab_the_codE5_sgOqkA}
```

