#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 23:14:00 2023

@author: maxrueda

Rueda, Maximillian
2/8/23
CSCI 2300
Lab 04

This code is a randomaized selection algorithm that returns the k-th smallest
 value of a randomized array
"""

import math
import random
import sys

sys.setrecursionlimit(1500)





def selection(n,k):
    S = []
    for i in range(n):
        S.append(random.randint(0, n))
    print("Main array:", S)
    print("")
    
    return selectionActual(S, k)

def selectionActual(S, k):
    v = random.choice(S)
    SL, Sv, SG = [], [],[]
    for val in S:
        if (val<v):
            SL.append(val)
        elif (val==v):
            Sv.append(val)
        elif (val>v):
            SG.append(val)
    
    print("SL:", SL)
    print("Sv:", Sv)
    print("SG:", SG)
    print("")
    
    if ( (len(SL)==0) and (len(SG)==0) ):
        return v
    
    if (k <= (len(SL))):
        return selectionActual(SL, k)
    elif ( (len(SL) < k) and (k <= (len(SL)+len(Sv))) ):
        return v
    elif (k > (len(SL)+len(Sv))):
        return selectionActual(SG, (k-len(SL)-len(Sv)))


print(selection(30, 5))




