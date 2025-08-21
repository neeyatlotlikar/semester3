import networkx as nx

# Create a sample undirected graph
G = nx.erdos_renyi_graph(10, 0.4, seed=42)

# Degree Centrality
deg_cent = nx.degree_centrality(G)
print("Degree Centrality:", deg_cent)

# Betweenness Centrality
btw_cent = nx.betweenness_centrality(G)
print("Betweenness Centrality:", btw_cent)

# Closeness Centrality
clo_cent = nx.closeness_centrality(G)
print("Closeness Centrality:", clo_cent)

# Eigenvector Centrality
eig_cent = nx.eigenvector_centrality(G, max_iter=1000)
print("Eigenvector Centrality:", eig_cent)

# Density
density = nx.density(G)
print("Density:", density)

# Clustering Coefficient (Global)
clustering = nx.transitivity(G)
print("Global Clustering Coefficient:", clustering)

# Diameter (only in connected graphs)
if nx.is_connected(G):
    diameter = nx.diameter(G)
    print("Diameter:", diameter)
else:
    print("Diameter: Graph is not connected.")
