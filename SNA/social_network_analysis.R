# Packages required
install.packages("igraph")
install.packages("ggraph")
install.packages("FactoMineR")
install.packages("intergraph")

# basic metrics
library(igraph)

g <- make_ring(5)

# The degree of a vertex is the number of its adjacent edges.
degree_central <- degree(g)
print(degree_central)

# number of (shortest paths) going through a vertex or an edge.
betweenness_central <- betweenness(g)
print(betweenness_central)

# measures how many steps are required to access every other vertex from a given vertex.
closeness_central <- closeness(g)
print(closeness_central)

# ratio of the actual number of edges and the largest possible number of edges in the graph
network_density <- edge_density(g)
print(network_density)

# probability that the adjacent vertices of a vertex are connected
cluster_coeff <- transitivity(g, type = "global")
print(cluster_coeff)

# Visualization With ggraph
library(ggraph)
library(tidygraph)

# data structure for tidy graph manipulation
tg <- as_tbl_graph(g)
ggraph(tg, layout = "fr") +
  geom_edge_link() +
  geom_node_point(size=5, color='steelblue') +
  geom_node_text(aes(label="Node"), repel=TRUE)

# Conversions
library(intergraph)
library(network)

# Convert objects to class "network"
net_g <- asNetwork(g)      # igraph → network
print(net_g)

# Coerce objects to class "igraph".
g_back <- asIgraph(net_g)  # network → igraph
print(g_back)


# Build a complex social graph
library(igraph)

# Create a random graph with 20 nodes & 45 edges.
set.seed(1234)
# Random graph with a fixed number of edges and vertices.
g <- sample_gnm(20, 45, directed=FALSE)

# Add node attributes: age & group
V(g)$age <- sample(18:50, vcount(g), replace=TRUE)
V(g)$group <- sample(c("TeamA", "TeamB", "TeamC"), vcount(g), replace=TRUE)

# Preview
print(g)


deg_central <- degree(g)
print(deg_central)


btw_central <- betweenness(g)
print(btw_central)


clo_central <- closeness(g)
print(clo_central)


net_density <- edge_density(g)
cluster_coeff <- transitivity(g, type = "global")
print(net_density)
print(cluster_coeff)


# Community Detection
# multi-level modularity optimization algorithm for finding community structure
comms <- cluster_louvain(g)
print(comms)
# results as an object from the communities class
print(membership(comms))


library(ggraph)
library(tidygraph)

tg <- as_tbl_graph(g)

ggraph(tg, layout = "fr") +
  geom_edge_link(alpha = 0.5) +
  geom_node_point(aes(color = group, size = age)) +
  #geom_node_text(aes(label = "x"), repel=TRUE, size=3) +
  ggtitle("Complex Social Network: Louvain Communities") +
  theme_void()


# Node Attribute Analysis
library(FactoMineR)

# Build a fake data frame of node attributes
data <- data.frame(
  age = V(g)$age,
  degree = deg_central,
  community = as.factor(membership(comms))
)
# Performs Principal Component Analysis
res.pca <- PCA(data, quali.sup=3, graph=TRUE)


# Subgraph Extraction
sub_g <- induced_subgraph(g, V(g)$group == "TeamA")
print(sub_g)
