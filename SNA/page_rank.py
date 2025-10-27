import networkx as nx


def pagerank_scratch(G, damping=0.85, max_iter=100, tol=1e-6):
    """
    Implements PageRank algorithm on a NetworkX directed graph G.
    Returns: dict of node: rank (importance score)
    """
    N = G.number_of_nodes()  # Total nodes
    ranks = dict.fromkeys(G, 1.0 / N)  # Initial uniform rank
    for _ in range(max_iter):
        new_ranks = {}
        for node in G:
            # Incoming links for node
            incoming_sum = sum(
                ranks[nbr] / G.out_degree(nbr)
                for nbr in G.predecessors(node)
                if G.out_degree(nbr) > 0
            )
            # PageRank formula with damping factor
            new_ranks[node] = (1 - damping) / N + damping * incoming_sum
        # Check convergence
        error = sum(abs(new_ranks[n] - ranks[n]) for n in G)
        ranks = new_ranks
        if error < tol:
            break
    return ranks


if __name__ == "__main__":
    # Create a sample directed graph
    G = nx.DiGraph()
    G.add_edges_from([("A", "B"), ("B", "C"), ("C", "A"), ("C", "D"), ("D", "B")])

    ranks_manual = pagerank_scratch(G)
    print("Manual PageRank:", ranks_manual)

    ranks_nx = nx.pagerank(G, alpha=0.85)
    print("NetworkX PageRank:", ranks_nx)
