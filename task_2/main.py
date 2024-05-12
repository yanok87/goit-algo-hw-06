"""This module uses the DFS and BFS algorithms to find paths in the graph"""

import argparse
from collections import deque
import networkx as nx


graph = {
    "Kyiv": ["Lutsk", "Lviv", "Warsaw", "Vienna"],
    "Lutsk": ["Lviv", "Warsaw"],
    "Lviv": ["Warsaw"],
    "Vienna": ["Munich"],
    "Munich": ["Warsaw"],
}

G = nx.Graph(graph)


def dfs_tree(graph, vertex, visited=None):
    """Depth first search function"""
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex)
    for neighbor in graph[vertex]:
        if (visited is not None) and (neighbor not in visited):
            dfs_tree(graph, neighbor, visited)


def bfs_tree(graph, queue, visited=None):
    """Breadth first search function"""
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex)
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_tree(graph, queue, visited)


def search_graph(algo_name: str):
    """Distinguish between DFS and BFS user input and call the respective algorythm func"""
    if algo_name == "dfs":
        dfs_tree(G, "Kyiv")

    elif algo_name == "bfs":
        bfs_tree(G, deque(["Kyiv"]))

    else:
        print("Such algorythm doesn't exist")


def main():
    """This function prompts user to enter a BFS of DFS algorythm name"""

    parser = argparse.ArgumentParser(
        description="Search pathes with BFS of DFS algorythm"
    )
    parser.add_argument("algo_name", type=str, help="Name of algorythm: DFS or BFS")

    args = parser.parse_args()
    algo_name = args.algo_name.lower()

    try:
        search_graph(algo_name)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    main()
