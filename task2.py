# DFS algorithm
def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(reversed(list(graph[vertex])))

    return path

# BFS algorithm
from collections import deque

def bfs_iterative(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    path = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(graph[vertex] - visited)

    return path

# Create the graph as adjacency list for DFS and BFS
graph_adj_list = {
    0: {1, 2, 3, 4, 5},
    1: {0, 11, 12},
    2: {0, 21, 22},
    3: {0, 31, 32},
    4: {0, 41, 42},
    5: {0, 51, 52},
    11: {1},
    12: {1},
    21: {2},
    22: {2},
    31: {3},
    32: {3},
    41: {4},
    42: {4},
    51: {5},
    52: {5},
}

# Run DFS and BFS
dfs_path = dfs_iterative(graph_adj_list, 0)
bfs_path = bfs_iterative(graph_adj_list, 0)

print(f"DFS Path: {dfs_path}")
print(f"BFS Path: {bfs_path}")
