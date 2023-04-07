#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:21:59 2023

@author: maxrueda

Rueda, Maximillian
2/28/23
CSCI 2300
Lab 07

This code uses the Dijkstra algorithm to read in information about a weighted,
 directed graph and using Breadth First Searching to return ...
"""


import math
import heapdict as hd



def Dijkstra(filename, source):
    Gv, Gw = {}, {}    #Gv = G, vertices ; Gw = G, weights
    for line in open(filename):
        u, v, weight = line.strip().split()
        u, v, weight = int(u), int(v), int(weight)
        tup = (u,v)
        
        if (u not in Gv.keys()):
            Gv[u] = [v]
        else:
            Gv[u].append(v)
        
        Gw[tup] = [weight]
    
    print(Gv, "\n" ,Gw)
    
    if (source not in Gv.keys()):
        print("Invalid Source Node")
        return
    
    
    dist, prev, pq = {}, {}, hd.heapdict()
    
    dist[source] = 0
    for key in Gv.keys():
        if (key != source):
            dist[key] = math.inf
    
    pq[source] = 0
    
    
    while pq:
        
        v, distance = pq.popitem()
        
        for u in Gv[v]:
            if ((v, u) not in Gw.keys()):
                continue
            path = dist[v] + Gw[(v, u)][0]
            if (path < dist[u]):
                
                dist[u] = path
                prev[u] = v
                
                pq[u] = path
     
        return dist



print(Dijkstra("lab07_test.txt", 1))
#Dijkstra("rome99.txt", 1)