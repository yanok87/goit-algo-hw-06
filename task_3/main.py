"""This module implement Dijkstra's algorithm"""

import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

# Travel Graph creation with the edges weight (travel time)
G.add_edge("Kyiv", "Lutsk", weight=4)
G.add_edge("Kyiv", "Lviv", weight=5)
G.add_edge("Kyiv", "Warsaw", weight=16)
G.add_edge("Kyiv", "Vienna", weight=25)
G.add_edge("Lutsk", "Lviv", weight=2)
G.add_edge("Lutsk", "Warsaw", weight=9)
G.add_edge("Lviv", "Warsaw", weight=8)
G.add_edge("Vienna", "Munich", weight=4)
G.add_edge("Munich", "Warsaw", weight=16)


# Visualise travel graph
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

# Find the shortest pathes between all cities
shortest_paths = {}
for start_node in G.nodes():
    shortest_paths[start_node] = {}
    for end_node in G.nodes():
        if start_node != end_node:
            shortest_paths[start_node][end_node] = nx.dijkstra_path_length(
                G, start_node, end_node
            )

print(shortest_paths)
