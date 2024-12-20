# R Stands Alone

> here's R, now cry about it.

## About the Challenge

This challenge uses RSA using 3 primes but r is a function of p and q. We are given the encryption script and the output consisting of r and ciphertext.

## Approach

These are the details we have 

    p , q -> two 512 bit primes

    r = p ^ 3 + 16 * q ^ 3 (r is a prime)

    e = 65537

    n = p * q * r

    ct = pow(flag, e, n)  # regular RSA

    Value of r, ct.

We need to get p and q using r.

1. My fist approach was to use sage's inbuilt solve functionality but that did not give me a clear answer as there were infinite results and it had no way of checking for primes simulatenously that i could find.

2. I found this paper (link [here](https://ora.ox.ac.uk/objects/uuid:ebb25eb4-a19e-4049-8117-3269e140b0fe/files/m4c54e951f8057c3650de2351e0f66eb5)) that spoke about primes of the form x^3 + 2 * y^3 but it seemed more focused on the number of such primes than their properties and also didnt say anything about x and y being primes.



