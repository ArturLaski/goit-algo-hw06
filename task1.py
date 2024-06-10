# Krok 1: Importowanie bibliotek
import networkx as nx
import matplotlib.pyplot as plt

# Krok 2: Tworzenie grafu
G = nx.Graph()

# Dodanie centralnego węzła i węzłów peryferyjnych
central_node = 0
G.add_node(central_node)
num_peripheral_nodes = 5

for i in range(1, num_peripheral_nodes + 1):
    G.add_node(i)
    G.add_edge(central_node, i)
    # Dodanie dwóch potomków do każdego węzła peryferyjnego
    child1 = i * 10 + 1
    child2 = i * 10 + 2
    G.add_node(child1)
    G.add_node(child2)
    G.add_edge(i, child1)
    G.add_edge(i, child2)

# Krok 3: Wizualizacja grafu
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
plt.title("Graf z centralnym węzłem i dwoma potomkami dla każdego węzła peryferyjnego")
plt.show()

# Krok 4: Analiza grafu
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Liczba węzłów: {num_nodes}")
print(f"Liczba krawędzi: {num_edges}")
print("Stopień każdego węzła:")
for node, degree in degrees.items():
    print(f"Węzeł {node}: {degree}")

# Wyświetlanie rozkładu stopni
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
plt.figure(figsize=(10, 8))
plt.bar(range(len(degree_sequence)), degree_sequence, color='skyblue')
plt.title("Rozkład stopni")
plt.xlabel("Węzeł")
plt.ylabel("Stopień")
plt.show()
