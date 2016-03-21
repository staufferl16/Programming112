"""
File: testcourses.py

Author: Leigh Stauffer
Project 12

Builds a graph of the courses in the CS curriculum at W&L
"""

from graph import LinkedDirectedGraph
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue
from grid import Grid
from arrays import Array

# Create a directed graph using an adjacency list.
chart = LinkedDirectedGraph()

# Add vertices with course labels and print the graph.
courseLyst = ["CSCI111", "CSCI210", "CSCI112",
            "CSCI209", "CSCI211", "CSCI312",
            "CSCI313", "MATH121", "MATH102",
            "MATH122", "MATH222"]
for item in courseLyst:
    chart.addVertex(item)

print("The chart: \n" + str(chart))

# Insert edges with weight 1 and print the graph.
chart.addEdge("CSCI111", "CSCI210", 1)
chart.addEdge("CSCI111", "CSCI112", 1)
chart.addEdge("CSCI210", "CSCI312", 1)
chart.addEdge("CSCI112", "CSCI209", 1)
chart.addEdge("CSCI112", "CSCI211", 1)
chart.addEdge("CSCI112", "CSCI312", 1)
chart.addEdge("MATH121", "CSCI211", 1)
chart.addEdge("MATH121", "MATH102", 1)
chart.addEdge("MATH121", "MATH122", 1)
chart.addEdge("MATH121", "CSCI313", 1)
chart.addEdge("MATH121", "CSCI312", 1)

print("The chart: \n" + str(chart))

# Print the vertices adjacent to vertex CSCI112.
v = chart.getVertex("CSCI112")
print("Expect vertices adjacent to CSCI112:")
for neighbor in chart.neighboringVertices(v.getLabel()):
    print(neighbor)

# Print the edges incident to CSCI112.
print("Expect edges incident to CSCI112:")
for edge in chart.incidentEdges(v.getLabel()):
    print(edge)

def traverseFromVertex(graph, startVertex, process, collection = LinkedStack()):
    chart.clearVertexMarks()
    collection.add(startVertex)
    while not collection.isEmpty():
        v = collection.pop()
        if not v.isMarked():
            v.setMark()
            process(v)
            for vertex in v.neighboringVertices():
                if not vertex.isMarked():
                    collection.add(vertex)

def depthFirstTraverse(graph, startVertex, process):
    traverseFromVertex(graph, startVertex, process, LinkedStack())


def breadthFirstTraverse(graph, startVertex, process):
    traverseFromVertex(graph, startVertex, process, LinkedQueue())


print("\nDepth first traversal:")
depthFirstTraverse(chart, chart.getVertex("CSCI111"), print)

print("\nBreadth first traversal:")
breadthFirstTraverse(chart, chart.getVertex("CSCI111"), print)

def topoSort(chart):  
    stack = LinkedStack()
    chart.clearVertexMarks()
    for v in chart.vertices():
        if not v.isMarked():
            dfs(chart, v, stack)
    return stack

def dfs(chart, v, stack):
    v.setMark()
    for w in v.neighboringVertices():
        if not w.isMarked():
            dfs(chart, w, stack)
    stack.push(v)

print("\nTopological sort:")
stack = topoSort(chart)
while not stack.isEmpty():
    print(stack.pop())

INFINITY = "-"

def makeLabelTable(graph):
    """Returns a table (dictionary) associating vetrex labels with
    index positions."""
    table = dict()
    index = 0
    for vertex in graph.vertices():
        table[vertex.getLabel()] = index
        index += 1
    return table

def makeDistanceMatrix(graph, table):
    """Returns a distance matrix for the given graph."""
    matrix = Grid(len(graph), len(graph), INFINITY)
    for vertex in graph.vertices():
        vertexLabel = vertex.getLabel()
        vertexIndex = table[vertexLabel]
        for neighbor in graph.neighboringVertices(vertexLabel):
            neighborLabel = neighbor.getLabel()
            neighborIndex = table[neighborLabel]
            weight = graph.getEdge(vertexLabel, neighborLabel).getWeight()
            print((vertexIndex, neighborIndex))
            matrix[vertexIndex][neighborIndex] = weight
    return matrix

def printDistanceMatrix(matrix, table):
    labels = Array(len(table))
    position = 0
    for label in table:
        labels[table[label]] = label
        position += 1
    print(" " * 9, " ".join(labels))
    print(end = " " * 13)
    for position in range(len(labels)):
        print(position, end = " " * 7)
    print("\n")
    for row in range(matrix.getHeight()):
        print(labels[row], row, end =" " * 4)
        for column in range(matrix.getWidth()):
            print(matrix[row][column], end = " " * 7)
        print()
            

print("\nLabel table for chart:")
labelTable = makeLabelTable(chart)
print(labelTable)


print("\nInitial distance matrix for chart:")
matrix = makeDistanceMatrix(chart, labelTable)
printDistanceMatrix(matrix, labelTable)

def allPairsShortestPaths(matrix):
    n = matrix.getWidth()
    for i in range(n):
        for r in range(n):
            for c in range (n):
                matrix[r][c] = minWithInfinity(matrix[r][c], addWithInfinity(matrix[r][i],
                                                                 matrix[i][c]))

def addWithInfinity(a, b):
    if a == INFINITY or b == INFINITY:
        return INFINITY
    else:
        return a + b

def minWithInfinity(a, b):
    if a == INFINITY and b != INFINITY:
        return b
    elif b == INFINITY and a != INFINITY:
        return a
    elif a == INFINITY and b == INFINITY:
        return INFINITY
    else:
        return min(a, b)
        
print("\nDistance matrix after running all pairs shortest paths:")
allPairsShortestPaths(matrix)
printDistanceMatrix(matrix, labelTable)

