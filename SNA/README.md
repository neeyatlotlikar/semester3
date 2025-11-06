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

3. ## Measures for Representing Social Networks

   Implementation of various measures for representing social networks. (Date: 12/08/2025)

4. ## Growth Models

   Implementation of various network growth models (Date: 29/08/2025)

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

   - They help expla in phenomena like viral content spread, academic citation patterns, and the emergence of hubs in social networks.
   - They’re foundational in fields like network science, epidemiology, and data science.

5. ## Social Network Data Collection

   Program to illustrate mechanism for collecting social networking data for different types of apps/networks (Ego networks and whole networks). Date: 21/08/2025

6. ## Social Media Data Processing

   Collect, analyze and aggregate social media data of twitter using python.
   Date: 04/09/2025

7. ## Online Social Networks Visualization

   Visualizing online social networks using tools/libraries
   Date: 18/09/2025

8. ## Random walks and their applications

   Random walks and their applications.
   Date: 22/09/2025

   Random walks are a fundamental mathematical tool used to extract information from the structure of complex networks, including social networks. They model the stochastic movement of a walker from one node to another, and their behavior can reveal important properties about the network, such as node centrality, community structure, and the flow of information or influence.
   In social network analysis, random walks are particularly valuable for tasks like ranking entities, identifying influential individuals, and detecting communities.

   One of the most well-known applications is Google's PageRank algorithm, which uses a personalized random walk to rank web pages based on their importance within the network.
   This concept extends to social networks for tasks like friend suggestion, where the similarity between users is measured by the likelihood of a random walk connecting them.
   Random walks also underpin various centrality measures, such as betweenness centrality based on the frequency with which a node is traversed by a random walk between other nodes, providing a more nuanced view than traditional shortest-path methods.

   Beyond ranking and centrality, random walks are applied in community detection. By analyzing the probability flow of random walks, researchers can identify densely connected groups or communities within a network, which is crucial for understanding the multipartite organization of social systems.
   They are also used in semi-supervised learning and network embedding, where the walk patterns help represent nodes in a lower-dimensional space while preserving structural relationships.

   Recent research has explored the use of random walks in more complex scenarios, such as analyzing multilayer networks to identify leaders in criminal networks, where classical and quantum random walks are used to define new centrality metrics based on node occupation.
   Furthermore, random walks are integral to recommendation systems, where biased random walks can incorporate social influence and user preferences to improve recommendation accuracy and mitigate cold-start problems.
   Despite their utility, random walks can be vulnerable to adversarial attacks, such as link deletion or addition, which can significantly alter the hitting time (time to reach a target node) and cover time (time to explore the entire network), highlighting the need for robust algorithms.

9. ## ontological representation of social individuals and relationships

   Aim: Implementation of ontological representation of social individuals and relationships.
   Date: 22/09/2025 (tentative)

10. ## Page Rank Algorithm

   Aim: Implementation of Page Rank Algorithms (Link Analysis).
   Date: 25/09/2025

11. ## Detecting communities in social networks

   Aim:  Detecting communities in social networks.
   Date: 03/11/25

12. ## cascading behaviour in social networks

   Aim: Demonstration of cascading behaviour in social networks
   Date: 03/11/25

   Code explained in brief
      - The code uses an Erdos-Renyi random graph as the social network.
      - Blue nodes are those who have adopted the new behavior ("A"), red nodes retain the old ("B").
      - Initial adopters (nodes 0 and 1) start the cascade.

13. ## GraphML

   Date: 06/11/2025

   GraphML is a standard XML-based file format used for storing and exchanging graph data, making it widely applicable in social network analysis and graph machine learning.
   It supports various graph types, including directed and undirected graphs, weighted and unweighted edges, and complex structures like multiple edges and nodes, which are essential for representing intricate social interactions.
   Social media platforms such as Twitter generate vast amounts of graph-structured data, where users are nodes and interactions like retweets, likes, and replies form the edges, making them among the largest producers of such data.
   These interactions can be modeled as large-scale complex graphs, enabling the application of graph machine learning (GraphML) techniques to uncover patterns and relationships.

   GraphML facilitates the creation and analysis of social networks by allowing data to be stored in a structured format that can be imported into visualization and analysis tools like Gephi or NodeXL.
   For instance, researchers and analysts can use tools such as NodeXL to collect Twitter data, create networks based on user interactions, and export the resulting graph to GraphML format for further analysis in Gephi.
   This process enables the visualization of social networks, where nodes represent users and edges represent interactions such as mentions, replies, or retweets, with directed and weighted edges capturing the nature and frequency of these interactions.

   Graph machine learning leverages these graph representations to perform tasks like community detection, link prediction, and node classification, which are crucial for understanding social dynamics.
   For example, analyzing a network of Twitter users can reveal influential individuals or tightly connected communities, as demonstrated by studies using tools like Gephi to visualize and rank nodes by in-degree, indicating how frequently users are mentioned or engaged with.
   Furthermore, GraphML supports advanced modeling using algorithms such as Graph Convolutional Networks (GCNs), Graph Attention Networks (GATs), and PageRank, which are used for tasks ranging from recommendation systems to detecting malicious behavior in social networks.

   The dynamic nature of social networks, where interactions evolve over time, requires models that can handle streaming data and changing structures, a challenge that current research in graph neural networks continues to address.
   By using GraphML to store and share graph data, researchers and developers can collaborate more effectively, ensuring interoperability across different platforms and tools.
   Overall, GraphML serves as a foundational format for representing, analyzing, and visualizing social networks, enabling deeper insights into user behavior and network structures.
