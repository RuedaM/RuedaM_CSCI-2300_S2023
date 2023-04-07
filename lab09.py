#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 07:54:17 2023

@author: maxrueda

Rueda, Maximillian
4/05/23
CSCI 2300
Lab 09

Implementation of the Dynamic Programming algorithm of chain matrix
 multiplication with the minimum number of operations.
"""



def MatrixChainOrder(arr):
    size = len(arr) - 1
    costs = [[0]*size for i in range(size)]
    order = [[0]*size for i in range(size)]
    
    for length in range(2, size+1):
        for i in range(size-length + 1):
            j = i + length - 1
            
            costs[i][j] = float("inf")
            for k in range(i, j):
                cost = costs[i][k] + costs[k+1][j] + arr[i] * arr[k+1] * arr[j+1]
                if (cost < costs[i][j]):
                    costs[i][j] = cost
                    order[i][j] = k
    
    return costs[0][size-1], order, size



def printOrder(optOrder, i, j):
    if (i==j):
        print(" A{}".format(i+1), end=' ')
    else:
        k = optOrder[i][j]
        print("(", end='')
        printOrder(optOrder, i, k)
        printOrder(optOrder, k+1, j)
        print(")", end='')





arr = [10, 20, 30, 40, 50, 40, 10, 50, 20]

ops, optOrder, size = MatrixChainOrder(arr)
print("Min number of ops:", ops)
print("Optimal Order:")
printOrder(optOrder, 0, size-1)