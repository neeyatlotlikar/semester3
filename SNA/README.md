# Social Network Analysis Lab Experiments

1. ## Python Networkx Library Study

2. ## Various tools for analysing social networks using R

   i graph, g-graph, factoMineR and intergraph in R

   Also important, need to implement SNA package.

   more on tools like gephi, ucinet, pajek, nodexl
   metric degree of centrality, betweenness cent, closeness cent and density, and cluster coeff
   cryptoscope, netlytic

   ego net analysis, whole net, two-node net, dynamic networks (temporal), multiplex, wighted, signed, bipartite

   Reference:
   Network visualization in R using i graph : Geeks for Geeks
   Udemy - SNA using R
   Videos: SNA with R by Dr. Bharatendra Rai, Tanmay Bhattacharya - SNA book

3. ## Growth Models

   Network growth models are mathematical frameworks used to understand how networks evolve over time by adding nodes and edges. Here are some of the most fundamental models:

   ### 📈 Basic Network Growth Models

   #### 1. **Uniform Random Attachment**

   - Each new node connects to an existing node chosen uniformly at random.
   - **Mechanism**: New nodes connect randomly to existing nodes.
   - **Outcome**: Degree distribution tends to be exponential.
   - **Limitation**: Doesn’t capture the heavy-tailed distributions seen in real-world networks like social or citation networks.

   #### 2. **Preferential Attachment (Barabási–Albert Model)**

   - Nodes are added one at a time and preferentially attach to existing nodes with high degree.
   - **Mechanism**: New nodes are more likely to connect to nodes that already have many connections.
   - **Outcome**: Produces a power-law (heavy-tailed) degree distribution.
   - **Real-world analogy**: “Rich-get-richer” effect—popular websites or influencers attract more links or followers.

   #### 3. **Multiplicative Growth Model**

   - Each node’s degree grows multiplicatively over time. This is more abstract, often used in weighted networks.
   - **Mechanism**: Objects (nodes) grow in size over time, with larger ones growing faster.
   - **Outcome**: Can lead to Pareto distributions, matching the skewness of real networks.
   - **Application**: Used in modeling economic or biological networks.

   #### 4. **Yule–Simon Model**

   - A model of preferential attachment with a probability of introducing new nodes vs reinforcing existing ones.
   - **Mechanism**: With some probability, a new node is added; otherwise, an existing node is duplicated or reused.
   - **Outcome**: Generates robust power-law distributions.
   - **Example**: Word frequency in documents—new words vs. repeated ones.

   #### 5. **Specialization Model**

   - Nodes specialize by duplicating and modifying their connections.
   - **Mechanism**: Selects a subset of nodes and evolves the network by specializing over those vertices.
   - **Outcome**: Can model complex real-world growth patterns.
   - **Use case**: Biological networks or evolving web graphs.

   #### 6. Erdős–Rényi Model (Random Graph)

   - This model adds edges between nodes randomly.

   #### 7. Watts–Strogatz Model (Small-World Network)

   - Starts with a regular lattice and rewires edges randomly to introduce shortcuts.

   #### 8. Ring Lattice

   - A regular graph where each node is connected to its 𝑘 nearest neighbors in a ring topology.

   #### 9. Prices Model

   - A precursor to the Barabási–Albert model, where nodes attach preferentially based on degree, but with a tunable initial attractiveness.

   #### 10. Local-World Model

   - Nodes attach preferentially within a randomly selected local subset of the network.

   #### 11. Edging in Preferential Attachment

   - A variation where new nodes connect preferentially, and additional edges are added between existing nodes.

   ### 🧠 Why These Models Matter

   - They help explain phenomena like viral content spread, academic citation patterns, and the emergence of hubs in social networks.
   - They’re foundational in fields like network science, epidemiology, and data science.
