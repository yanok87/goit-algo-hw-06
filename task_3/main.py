"""This module implement Dijkstra's algorithm"""

# Define the graph as a dictionary with nodes as keys and their neighbors and weights as values

graph = {
    "Kyiv": {"Lutsk": 4, "Lviv": 5, "Warsaw": 16, "Vienna": 25},
    "Lutsk": {"Kyiv": 4, "Lviv": 2, "Warsaw": 9},
    "Lviv": {"Kyiv": 5, "Lutsk": 2, "Warsaw": 8},
    "Warsaw": {"Kyiv": 16, "Lutsk": 9, "Lviv": 8, "Munich": 16},
    "Vienna": {"Kyiv": 25, "Munich": 4},
    "Munich": {"Vienna": 4, "Warsaw": 16},
}


def dijkstra(graph, start):
    """Dijkstra algorithm to find the shortest pathes"""
    # Initialize distances from the start node to all other nodes as infinity
    distances = {node: float("inf") for node in graph}
    # Distance from the start node to itself is 0
    distances[start] = 0
    # Initialize an empty set to keep track of visited nodes
    visited = set()

    while len(visited) < len(graph):
        # Find the node with the smallest distance from the start node
        current_node = min(
            (node for node in graph if node not in visited), key=lambda x: distances[x]
        )
        visited.add(current_node)
        # Update distances to neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight

    return distances


shortest_paths_from_kyiv = dijkstra(graph, "Kyiv")
print("Shortest paths from Kyiv:")
print(shortest_paths_from_kyiv)
