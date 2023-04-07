#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:35:55 2023

@author: maxrueda

Rueda, Maximillian
3/29/23
CSCI 2300
Lab 08

This is an implementation of Prim's algorithm on a given undirected graph with
 weighted edges


prim(graph):
    # Initialize an empty set to hold the vertices in the minimum spanning tree
    mst = empty set

    # Select the first vertex to start the tree
    startVertex = first vertex in graph
    mst.add(startVertex)

    # Initialize the set of edges to consider
    edges = edges connected to startVertex

    # Iterate until all vertices are in the minimum spanning tree
    while mst has fewer vertices than graph:
        # Find the minimum edge in the set of edges
        minEdge, minWeight = findMinEdge(edges)

        # Add the vertex to the minimum spanning tree
        mst.add(minEdge)

        # Add the edges connected to the vertex to the set of edges to consider
        for edge in edges connected to minEdge:
            if edge is not in mst:
                edges.add(edge)

        # Remove the minimum edge from the set of edges to consider
        edges.remove(minEdge)

    # Return the minimum spanning tree as an array
    return mst as an array
"""

def findMinEdge(edges):
    print("")
    print("START findMinEdge")
    minWeight = 1000
    minEdge = None

    for tup in edges:
        print("Looking at", tup[0], tup[1], tup[2])
        if ((tup[0] in U) or (tup[1] in U)):
            print("No good: one vertex is leaf")
            continue
        if (tup[2] < minWeight):
            print(tup[2], "is less than", minWeight)
            minEdge = tup
            minWeight = tup[2]
    
    print("Final minEdge:", minEdge)
    print("FINISH findMinEdge")
    print("")
    return minEdge

def findMinEdge2(edges, vertex):
    print("")
    print("START findMinEdge2")
    minWeight = 1000
    minEdge = None

    for tup in edges:
        print("Looking at", tup[0], tup[1], tup[2])
        if (tup[2] < minWeight) and ((tup[0]==vertex) or (tup[1]==vertex)):
            print(tup[2], "is less than", minWeight)
            minEdge = tup
            minWeight = tup[2]
    
    print("Final minEdge:", minEdge)
    print("FINISH findMinEdge2")
    print("")
    return minEdge



V = {"A","B","C","D","E","F","G","H","I"}
E = {("A","B",10), ("A","C",12), ("B","C",9), ("B","D",8), ("C","E",3),
     ("C","F",1), ("D","E",7), ("D","G",8), ("D","H",5), ("E","F", 3),
     ("F","H",6), ("G","H",9), ("G","I",2), ("H","I",11)}
U={"A", "D", "F"}

Enew = {("E", "H", 3)}



mst = set()
mstEdges = set()
edges = set()

V = V - U
E = E.union(Enew)

start = "H"
mst.add(start)

print("V:", V)
print("E:", E)
print("mst:", mst)
print("mstEdges:", mstEdges)
print("edges:", edges)
print("start: ", start)

print("\n")


for tup in E:
    if ((tup[0] == start) or (tup[1] == start)):
        edges.add(tup)
print("Edges of start:", edges)


while(len(mst)<len(V)):
    
    minEdge = findMinEdge(edges)
    if (minEdge == None):
        break

    mst.add(minEdge[0])    
    mst.add(minEdge[1])
    mstEdges.add(minEdge)
    
    
    print("CURRENT MST:", mst)
    print("CURRENT MST EDGES:", mstEdges)
    
    mrv = None
    if (minEdge[1] in mst):
        mrv = minEdge[0]
    else:
        mrv = minEdge[1]
    print("Most recent vertex:", mrv)
    print("")
    
    print("Looking for edges with", mrv)
    for tup in E:
        print("Looking at", tup[0], tup[1], tup[2])
        if ((tup[0] == mrv) or (tup[1] == mrv)):
            print("There is a match")
            if (tup not in mstEdges):
                edges.add(tup)
    
    edges.remove(minEdge)
    print("New edges:", edges)

print("")
print("FINISHED, almost")
print(mst)
print(mstEdges)

if (len(mst) != len(V)):
    print("No solution, idiot")
    quit()

print("Now add leaves")
edges.clear()

for vertex in U:
    print("Finding edges with", vertex)
    for tup in E:
        print("Looking at", tup[0], tup[1], tup[2])
        if ((tup[0] == vertex) or (tup[1] == vertex)):
            print("There is a match")
            edges.add(tup)
    
    print("Edges:", edges)
    
    minEdge = findMinEdge2(edges, vertex)
    mst.add(minEdge[0])    
    mst.add(minEdge[1])
    mstEdges.add(minEdge)
    
print("")
print("FINISHED")
print(mst)
print(mstEdges)