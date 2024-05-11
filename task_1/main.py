"""This module creates a real-world travel network"""

import networkx as nx
import matplotlib.pyplot as plt


# Travel Graph creation
graph = {
    "Kyiv": ["Lutsk", "Lviv", "Warsaw", "Vienna"],
    "Lutsk": ["Lviv", "Warsaw"],
    "Lviv": ["Warsaw"],
    "Vienna": ["Munich"],
    "Munich": ["Warsaw"],
}

G = nx.Graph(graph)

nx.draw(G, with_labels=True)
plt.show()

# Analysis of the Travel Graph
num_nodes = G.number_of_nodes()
print(num_nodes)  # 6

num_edges = G.number_of_edges()
print(num_edges)  # 9

is_connected = nx.is_connected(G)
print(is_connected)  # True

degree_centrality = nx.degree_centrality(G)
print(
    degree_centrality
)  # {'Kyiv': 0.8, 'Lutsk': 0.6000000000000001, 'Lviv': 0.6000000000000001, 'Warsaw': 0.8, 'Vienna': 0.4, 'Munich': 0.4}

closeness_centrality = nx.closeness_centrality(G)
print(
    closeness_centrality
)  # {'Kyiv': 0.8333333333333334, 'Lutsk': 0.7142857142857143, 'Lviv': 0.7142857142857143, 'Warsaw': 0.8333333333333334, 'Vienna': 0.625, 'Munich': 0.625}

betweenness_centrality = nx.betweenness_centrality(G)
print(
    betweenness_centrality
)  # {'Kyiv': 0.25, 'Lutsk': 0.0, 'Lviv': 0.0, 'Warsaw': 0.25, 'Vienna': 0.05, 'Munich': 0.05}
