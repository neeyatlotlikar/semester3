import networkx as nx
import random


def random_walk(graph, start_node, steps):
    current_node = start_node
    walk_path = [current_node]

    for _ in range(steps):
        neighbors = list(graph.neighbors(current_node))
        if not neighbors:
            break  # Dead end, stop walking
        current_node = random.choice(neighbors)
        walk_path.append(current_node)

    return walk_path


# Example usage
if __name__ == "__main__":
    # Create a sample social network graph
    G = nx.Graph()

    # Add nodes (people)
    G.add_nodes_from(["A", "B", "C", "D", "E"])

    # Add edges (social connections)
    G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")])

    start = "A"
    steps = 10

    path = random_walk(G, start, steps)
    print("Random walk path:", path)
