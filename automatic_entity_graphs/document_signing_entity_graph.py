import networkx as nx
import matplotlib.pyplot as plt

# 1. Initialize the Directed Graph
G = nx.DiGraph()

# 2. Define Nodes based on the plan
# Node names are used as keys. We'll store their types for styling.
nodes = {
    "post": {"type": "B-object", "label": "Facebook Post"},
    "biden": {"type": "B-object", "label": "Joe Biden"},
    "quote": {"type": "B-object", "label": "Quote:\n\"I don’t know what\nI’m signing\""},
    "attribution": {"type": "B-relationship", "label": "Attribution"},
    "verdict": {"type": "Verdict", "label": "FALSE UTTERANCE"}
}

# Add nodes to the graph
for node, attrs in nodes.items():
    G.add_node(node, type=attrs['type'], label=attrs['label'])

# 3. Define Edges with labels based on the plan
edges = [
    ("post", "attribution", "makes"),
    ("attribution", "biden", "agent"),
    ("attribution", "quote", "content"),
    ("verdict", "attribution", "refutes")
]

# Add edges to the graph
for source, target, label in edges:
    G.add_edge(source, target, label=label)

# 4. Define Visual Properties
node_colors_map = {
    "B-object": "skyblue",
    "B-relationship": "lightgreen",
    "Verdict": "lightgrey"
}

node_shapes_map = {
    "B-object": 's',  # 's' for square/rectangle
    "B-relationship": 'D',  # 'D' for diamond/rhombus
    "Verdict": 's'
}

# Assign colors and shapes to each node in the graph
node_colors = [node_colors_map[G.nodes[n]['type']] for n in G.nodes()]
node_shapes_set = set(node_shapes_map.values()) # a set of unique shape markers

# Create a mapping from node name to its label for drawing
labels = {n: G.nodes[n]['label'] for n in G.nodes()}
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}

# 5. Define Layout for Readability
# Start with a spring layout and then manually adjust for clarity
pos = nx.spring_layout(G, seed=42, k=2.0)

# Manual adjustments to prevent overlap and improve flow
pos['attribution'] = [0, 0]
pos['post'] = [-0.8, 0]
pos['biden'] = [0.8, 0.4]
pos['quote'] = [0.8, -0.4]
pos['verdict'] = [0, -0.8]

# 6. Draw the Graph
plt.figure(figsize=(12, 9))
plt.title("Argumentation Graph: 'Biden Quote' Fact-Check", fontsize=16)

# Draw nodes one shape at a time
for shape in node_shapes_set:
    # Get all nodes with the current shape
    nodelist = [node for node, attrs in G.nodes(data=True) if node_shapes_map[attrs['type']] == shape]
    # Get their corresponding colors
    colorlist = [node_colors_map[attrs['type']] for node, attrs in G.nodes(data=True) if node_shapes_map[attrs['type']] == shape]

    nx.draw_networkx_nodes(G, pos,
                           nodelist=nodelist,
                           node_shape=shape,
                           node_color=colorlist,
                           node_size=6000, # Increased size for readability
                           edgecolors='black')

# Draw edges
nx.draw_networkx_edges(G, pos,
                       width=1.5,
                       arrowstyle='-|>',
                       arrowsize=20,
                       edge_color='gray',
                       node_size=6000) # Match node_size to avoid overlap

# Draw node and edge labels
nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color='red')

# 7. Display the Plot
plt.box(False)
plt.show()

