"""This module uses the DFS and BFS algorithms to find paths in the graph"""

import networkx as nx
import argparse


graph = {
    "Kyiv": ["Lutsk", "Lviv", "Warsaw", "Vienna"],
    "Lutsk": ["Lviv", "Warsaw"],
    "Lviv": ["Warsaw"],
    "Vienna": ["Munich"],
    "Munich": ["Warsaw"],
}

G = nx.Graph(graph)


# DFS function
dfs_tree = nx.dfs_tree(G, source="Kyiv")
# [('Kyiv', 'Lutsk'), ('Lutsk', 'Lviv'), ('Lviv', 'Warsaw'), ('Warsaw', 'Munich'), ('Munich', 'Vienna')]

# BFS function
bfs_tree = nx.bfs_tree(G, source="Kyiv")
# [('Kyiv', 'Lutsk'), ('Kyiv', 'Lviv'), ('Kyiv', 'Warsaw'), ('Kyiv', 'Vienna'), ('Warsaw', 'Munich')]


def search_graph(algo_name: str):
    """Distinguish between DFS and BFS user input and call the respective algorythm func"""
    if algo_name == "dfs":
        print("Pathes found:", list(dfs_tree.edges()))

    elif algo_name == "bfs":
        print("Pathes found:", list(bfs_tree.edges()))

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
