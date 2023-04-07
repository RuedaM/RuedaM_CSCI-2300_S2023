#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:07:15 2023

@author: maxrueda

Rueda, Maximillian
2/15/23
CSCI 2300
Lab 05

This code implements a quicksort algorithm that splits an array into 3 parts:
 an array of a specified random median, an array of values less than the median,
 and an array of values greater than the median. After multiple recursions, it
 will sort the array
"""



import math
import random





def quicksort(S):
    
    v = random.choice(S)
    SL, Sv, SG = [], [],[]
    for val in S:
        if (val<v):
            SL.append(val)
        elif (val==v):
            Sv.append(val)
        elif (val>v):
            SG.append(val)
    
    print("")
    print("SL:\n", SL)
    print("Sv:\n", Sv)
    print("SG:\n", SG)
    print("")
    
    if ( (len(SL)==0) and (len(SG)==0) ):
        return S
    
    SNew = []
    if (len(SL) != 0):
        print("Entering left recursion...")
        SLNew = quicksort(SL)
        SNew+=SLNew
    print("SNew so far:", SNew)
    SNew+=Sv
    print("SNew so far:", SNew)
    if (len(SG) != 0):
        print("Entering right recursion...")
        SGNew = quicksort(SG)
        SNew+=SGNew
    
    return SNew



vals = []
n = random.randint(1,100)
while (len(vals) < n):
    vals.append(random.randint(0,n-1))

print("MAIN ARRAY:\n", vals)

print("RESULT:\n", quicksort(vals))