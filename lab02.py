#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:06:31 2023

@author: maxrueda

Rueda, Maximillian
1/25/23
CSCI 2300
Lab 02

This code ccompares 3 different versions of integer multiplication: the first is
 "vertical multiplication" as done in elementary school, the second is recursive,
 and the last implements a "divide and conquer" algorithm
"""

import math
import time
import random


 
def Method1(x, y):
    yBin = bin(y)
    yBinLen = y.bit_length()
    
    intermediates = []
    product = 0
    
    for i in (range(1, yBinLen+1)):
        if (yBin[i]!=0):
            intermediates.append(x << (yBinLen+1-i))
            product += intermediates[-1]
    
    return product


def Method2(x,y):
    if (y==0): return 0
    
    product = Method2(x, math.floor(y>>1))
    
    if (y%2==0):
        return (product<<1)
    else:
        return (x+(product<<1))


def Method3(x,y):
    n = max(int(x.bit_length()), int(y.bit_length()))
    
    x >>= 1
    
    if (n==1): return x*y
    
    xL, xR = x >> math.ceil(n>>1), x & ((1 << math.floor(n>>1)) - 1)
    yL, yR = y >> math.ceil(n>>1), y & ((1 << math.floor(n>>1)) - 1)
    
    p1 = Method3(xL, yL)
    p2 = Method3(xR, yR)
    p3 = Method3(xL+xR, yL+yR)
    product = (p1 << (math.floor(n>>1) << 1)) + ((p3-p1-p2) << math.floor(n>>2)) + p2
    
    return product


def generate(d):
    digits = int("9"*d)


    valList = []
    print("Factors and digit counts:")
    for i in range(10):
        boolFlag = True
        while boolFlag:
            x = random.randint(1, digits)
            y = random.randint(1, digits)
            if (len(str(x))==len(str(y)) and (len(str(x))==len(str(digits)))):
                boolFlag = False
        
        tup = (x, y)
        print(tup)
        valList.append((x, y))
    
    return valList



d = int(input("Give number of digits: "))

valList = generate(d)

print("")

timeList = []
for i in range(10):
    Time1 = time.time()
    Method1(valList[i][0], valList[i][1])
    Time1 = time.time() - Time1
    Time2 = time.time()
    Method1(valList[i][0], valList[i][1])
    Time2 = time.time() - Time2
    Time3 = time.time()
    Method1(valList[i][0], valList[i][1])
    Time3 = time.time() - Time3
    
    timeList.append((Time1, Time2, Time3))

for i in range(3):
    timeSum = 0
    avg = 0
    for j in range(len(timeList)):
        timeSum += timeList[j][i]
        avg = timeSum/len(timeList)
    print("Avg. time for Method", i+1, "is:", avg)