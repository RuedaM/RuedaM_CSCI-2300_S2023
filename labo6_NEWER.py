#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:32:41 2023

@author: maxrueda
"""

file1 = open('LAB6-TEST-SET-SMALL.txt','r')
file2 = open('LAB6-TEST-SET.txt','r')

G = {}
Gr = {}
stack = []
visited = {}

lines = file1.readlines()
for line in lines:
    vertex, next = line.strip().split()
    vertex, next = int(vertex), int(next)
    
    if vertex not in G:
        G[vertex] = [next]
        visited[vertex] = False
    else:
        G[vertex].append(next)

    if next not in Gr:
        Gr[next] = [vertex]
        visited[next] = False
    else:
        Gr[next].append(vertex)

def fill_order(index, visited, stack):
    visited[index] = True
    if index not in G:
        pass
    else:
        for j in G[index]:
            if visited[j] == False:
                fill_order(j, visited, stack)
    stack.append(index)

def dfs(index, visited):
    visited[index] = True
    print(index,end=' ')
    if index not in Gr:
        pass
    else:
        for m in Gr[index]:
            if visited[m] == False:
                dfs(m, visited)

for i in G:
    if visited[i] == False:
        fill_order(i, visited, stack)
for k in visited:
    visited[k] = False
while len(stack) > 0:
    l = stack.pop()
    if visited[l] == False:
        dfs(l, visited)
        print("")