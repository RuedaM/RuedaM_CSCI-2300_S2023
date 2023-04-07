#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:48:02 2023

@author: maxrueda

Rueda, Maximillian
1/18/23
CSCI 2300
Lab 01

This code computes the nth number of the Fibonacci sequence both recursively and
 iteratively. Times to calculate the value both ways are given.
"""

import time
import timeit


def FibRecursive(n):
    if (n==0): return 0
    elif (n==1): return 1
    else: return (FibRecursive(n-1)+FibRecursive(n-2))

def FibIterative(n):
    a,b = 0,1
    for i in range(n): a,b = b, a+b
    return a


values = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41, 42, 43]


print()
print("Calculating...")
print()

for n in values:
    print("INPUT VALUE:", n)
    TempI = time.time()
    FibI = FibIterative(n)
    TimeI = time.time() - TempI
    print("Iterative Fibonacci result: {}".format(FibI))
    print("Time to calculate: {} seconds".format(TimeI))
    #print("Time: ", timeit.timeit('FibIterative(n)'))
    print()
    TempR = time.time()
    FibR = FibRecursive(n)
    TimeR = time.time() - TempR
    print("Recursive Fibonacci result: {}".format(FibR))
    print("Time to calculate: {} seconds".format(TimeR))
    #print("Time: ", timeit.timeit('FibRecursive(n)'))
    print("----------")


values2 = [2**10, 2**12, 2**14, 2**16, 2**18, 2**19]
for n in values2:
    print("INPUT VALUE:", n)
    TempI = time.time()
    FibI = FibIterative(n)
    TimeI = time.time() - TempI
    #print("Iterative Fibonacci result: {}".format(FibI))
    print("Time to calculate: {} seconds".format(TimeI))
    #print("Time: ", timeit.timeit('FibIterative(n)'))
    print("----------")
