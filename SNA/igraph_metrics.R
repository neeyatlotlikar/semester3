library(igraph)

# Create a random undirected graph
set.seed(42)
g <- erdos.renyi.game(10, 0.4)

# Degree Centrality
deg_cent <- degree(g)
print(deg_cent)

# Betweenness Centrality
btw_cent <- betweenness(g)
print(btw_cent)

# Closeness Centrality
clo_cent <- closeness(g)
print(clo_cent)

# Eigenvector Centrality
eig_cent <- eigen_centrality(g)$vector
print(eig_cent)

# Density
density <- edge_density(g)
print(density)

# Clustering coefficient (transitivity)
cluster_coeff <- transitivity(g, type="global")
print(cluster_coeff)

# Diameter
if (is.connected(g)) {
  diameter_g <- diameter(g)
  print(diameter_g)
} else {
  print("Graph is not connected; diameter not defined.")
}

