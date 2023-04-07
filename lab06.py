#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:30:28 2023

@author: maxrueda

Rueda, Maximillian
2/22/23
CSCI 2300
Lab 06

This code implements a linear time strongly connected components algorithm.
 Given a directed graph G, a reverse graph G^R is created in linear time. Next,
 the undirected connected components method is run, processing the vertices in
 decreasing post order.
"""



def fileparse(filename, G, Gr):
    for line in open(filename):
        v, u = line.strip("\n").split(" ")
        v, u = int(v), int(u)
        
        if (v in G):
            G[v].append(u)
        else:
            G[v] = [u]
            G[v].append(u)
        
        if (u in Gr):
            Gr[u].append(v)
        else:
            Gr[u] = [v]
            Gr[u].append(v)
    
    return G, Gr



def DFS(aL, vSet, sSet, key):
    if (key not in aL.keys()):
        return
    
    if (key not in vSet):
        vSet.append(key)
        for val in aL[key]:
            DFS(aL, vSet, sSet, val)
        sSet.append(key)
        
    

def DFSReverse(aLR, vSet, sSet, key):
    print(vSet)
    print(sSet)
    print(key)
    
    sSet.pop()
    
    if (key not in vSet):
        print(key, "not in vSet yet")
        vSet.append(key)
        
        if (key not in aLR.keys()):
            print(key, "not found in dict")
            DFSReverse(aLR, vSet, sSet, sSet[-1])
        else:
            print(key, "is key in dict")
            for val in aLR[key]:
                DFSReverse(aLR, vSet, sSet, val)
    else:
        print(key, "already in vSet")
            




a, b, c, d = dict(), dict(), dict(), dict()
GSmall, GrSmall = fileparse("LAB6-TEST-SET-SMALL.txt", a, b)
print("GSmall:\n", GrSmall)
print("GrSmall:\n", GrSmall)

visitedSet, stackSet = [], []
DFS(GrSmall, visitedSet, stackSet, list(GrSmall.keys())[0])
print("")
print("visitedSet:", visitedSet)
print("stackSet:", stackSet)
visitedSet.clear()
print("")
print("visitedSet:", visitedSet)
print("stackSet:", stackSet)
DFSReverse(GrSmall, visitedSet, stackSet, stackSet[-1])
print("")
print("visitedSet:", visitedSet)
print("stackSet:", stackSet)