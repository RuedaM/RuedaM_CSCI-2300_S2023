#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:59:03 2023

@author: maxrueda

Rueda, Maximillian
2/1/23
CSCI 2300
Lab 03

This code implements a modular exponentiation function that takes 3 inputs as
 well as a randomized primality testing algorithm that uses the previously
 mentioned exponentiation function.
"""

import random
import math



def modexp(x, y, N):
    if (y==0): return 1
    
    z = modexp(x, math.floor(y/2), N)
    
    if (y%2==0): return z**2 % N
    else: return x * z**2 % N


def randomprime(N, k):
    P = 0.0;
    C = 0.0;
    for i in range(1, k):
        a = random.randint(1, N)
        
        if (modexp(a, N-1, N) == 1 % N):
            P+=1
        else:
            C+=1
    
    if (P>C):
        print(N, "is Prime.")
    else:
        print(N, "is Composite.")


def randomprimeCar(N, k):
    P = 0.0;
    C = 0.0;
    for i in range(1, k):
        a = random.randint(1, N)
        
        if (modexp(a, N-1, N) == 1 % N):
            P+=1
        else:
            C+=1
    return P/C





vals = []
while (len(vals) < 3):
    n = random.randint(1, 99)
    if (n>9): vals.append(n)

k = 50
for val in vals:
    randomprime(val,k)

#-----------------------------------------------------------------------------
print("\n\n\n")
#-----------------------------------------------------------------------------

Carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341,
              41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217,
              162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153,
              340561, 399001, 410041, 449065, 488881]
k = 1000

print("Value of 1/(2^k) if k=1000:", 1/(2**k))
print("")
for val in Carmichael:
    print("Prob. of failure for {} is: {:.3f}%".format(val, randomprimeCar(val, k)))