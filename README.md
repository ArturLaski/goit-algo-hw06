# Homework: Graph Algorithms

## Introduction

This homework demonstrates the use of Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms to find paths in a graph. The graph is constructed to represent a network where each node, except the central node, has two children.

## Graph Description

The graph is created as follows:
- A central node (0) connected to 5 peripheral nodes (1 to 5).
- Each peripheral node has two children.

## DFS and BFS Implementations

### DFS (Depth-First Search)

DFS explores as far as possible along each branch before backtracking. It uses a stack to keep track of the nodes to be explored next.

### BFS (Breadth-First Search)

BFS explores all neighbors of a node before moving to the next level of neighbors. It uses a queue to keep track of the nodes to be explored next.

## Results

- **DFS Path**: `[0, 5, 52, 51, 4, 42, 41, 3, 32, 31, 2, 22, 21, 1, 12, 11]`
- **BFS Path**: `[0, 1, 2, 3, 4, 5, 11, 12, 21, 22, 31, 32, 41, 42, 51, 52]`

## Comparison and Explanation

- **DFS Path**: DFS goes deep into the graph, exploring each node's children before moving to the next sibling node. This results in a path that goes from the central node to a peripheral node, then to its children before backtracking.
  
- **BFS Path**: BFS explores all nodes at the current level before moving to the next level. This results in a path that includes all peripheral nodes connected to the central node first, followed by their children level by level.

The difference in paths is due to the nature of the two algorithms. DFS prioritizes depth, while BFS prioritizes breadth.

## Conclusion

Both DFS and BFS are essential graph traversal algorithms with distinct strategies. Understanding their differences is crucial for selecting the appropriate algorithm based on the specific requirements of a problem.


# Homework: Graph Algorithms with Dijkstra's Algorithm

## Introduction

This part of the homework demonstrates the use of Dijkstra's algorithm to find the shortest paths in a weighted graph. The graph is constructed to represent a network where each node, except the central node, has two children, and each edge has a weight.

## Graph Description

The graph is created as follows:
- A central node (0) connected to 5 peripheral nodes (1 to 5).
- Each peripheral node has two children.
- Each edge has a specific weight.

## Dijkstra's Algorithm Implementation

Dijkstra's algorithm finds the shortest paths from a given start vertex to all other vertices in the graph. It uses a priority queue to explore the nodes with the smallest known distance first.

## Results

### Shortest Paths
