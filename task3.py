import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Create the graph with each node having 2 children and add weights
G = nx.Graph()
central_node = 0
G.add_node(central_node)
num_peripheral_nodes = 5

edges_with_weights = []

for i in range(1, num_peripheral_nodes + 1):
    weight_to_peripheral = i  # Weight from central node to peripheral node
    edges_with_weights.append((central_node, i, weight_to_peripheral))
    
    child1 = i * 10 + 1
    child2 = i * 10 + 2
    weight_to_child1 = i + 1  # Arbitrary weight to first child
    weight_to_child2 = i + 2  # Arbitrary weight to second child
    
    edges_with_weights.append((i, child1, weight_to_child1))
    edges_with_weights.append((i, child2, weight_to_child2))

# Add edges with weights to the graph
G.add_weighted_edges_from(edges_with_weights)

# Visualize the graph with weights
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Graph with Weights")
plt.show()

# Dijkstra's algorithm
def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Find shortest paths from all vertices
shortest_paths = {}
for vertex in G.nodes:
    shortest_paths[vertex] = dijkstra(G, vertex)

# Display the shortest paths
for start_vertex, distances in shortest_paths.items():
    print(f"Shortest paths from vertex {start_vertex}:")
    for end_vertex, distance in distances.items():
        print(f"  to vertex {end_vertex}: {distance}")
    print()

