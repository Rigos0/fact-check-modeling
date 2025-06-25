import networkx as nx
import matplotlib.pyplot as plt

# --- 1. SETUP GRAPH AND DEFINE COMPONENTS ---

# Create a directed graph
G = nx.DiGraph()

# Define nodes and their properties (label and type)
# Using short names for node IDs and full text for labels
node_specs = {
    'contrast': {'label': 'Performance\nContrast', 'type': 'B-relationship'},
    'ev': {'label': 'Electric Vehicles\n(EVs)', 'type': 'B-object'},
    'gas': {'label': 'Gasoline Vehicles', 'type': 'B-object'},
    'context': {'label': 'Context:\nSnowstorm Traffic Jam', 'type': 'B-Attribute'},
    'metric': {'label': 'Metric:\nReliability', 'type': 'B-Attribute'},
    'verdict': {'label': '<FALSE CONTRAST>', 'type': 'Verdict-or-Note'}
}

# Define visual properties based on component type
visual_map = {
    'B-object': {'color': 'skyblue', 'shape': 's', 'style': 'square,pad=0.8'},
    'B-relationship': {'color': 'lightgreen', 'shape': 'd', 'style': None},
    'B-Attribute': {'color': 'orange', 'shape': 's', 'style': 'square,pad=0.6'},
    'Verdict-or-Note': {'color': '#cccccc', 'shape': 's', 'style': 'square,pad=0.5'}
}

# Add nodes to the graph
for node_id, properties in node_specs.items():
    G.add_node(node_id, label=properties['label'], type=properties['type'])

# Define edges and their labels
edges = [
    ('contrast', 'ev', 'subject'),
    ('contrast', 'gas', 'object of comparison'),
    ('contrast', 'context', 'in context of'),
    ('contrast', 'metric', 'on metric of'),
    ('verdict', 'contrast', 'refutes')
]

# Add edges to the graph
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# --- 2. DEFINE LAYOUT AND VISUALS ---

# Manually define node positions for optimal readability and no overlaps
pos = {
    'contrast': (0, 0),
    'ev': (-1.5, 0.8),
    'gas': (-1.5, -0.8),
    'context': (1.5, 0.8),
    'metric': (1.5, -0.8),
    'verdict': (0, 1.5)
}

# Prepare lists of nodes for each type for separate drawing
nodes_by_type = {v['type']: [] for v in node_specs.values()}
for node, data in G.nodes(data=True):
    nodes_by_type[data['type']].append(node)

# Prepare labels for nodes and edges
node_labels = nx.get_node_attributes(G, 'label')
edge_labels = nx.get_edge_attributes(G, 'label')

# --- 3. DRAW THE GRAPH ---

# Create the plot
plt.figure(figsize=(14, 10))
plt.title("Visual Argumentation: Fact-Check Analysis", fontsize=16, fontweight='bold')

# Draw the edges with arrows
nx.draw_networkx_edges(
    G,
    pos,
    edge_color='gray',
    width=1.5,
    arrowsize=20,
    node_size=3000, # Increase node_size to shorten edges from node center
    connectionstyle='arc3,rad=0.1' # Slightly curve the edges
)

# Draw the edge labels
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color='black',
    font_size=9,
    bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', pad=1)
)

# Draw each node type with its specific style
# The 'bbox' approach for labels creates the rectangular node shapes
for node_type, nodes in nodes_by_type.items():
    if not nodes:
        continue
    
    style_info = visual_map[node_type]
    
    # The relationship (rhombus) is drawn as a node, others as label bounding boxes
    if style_info['style'] is None: # This is the B-relationship rhombus
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=nodes,
            node_shape=style_info['shape'],
            node_color=style_info['color'],
            node_size=6000,
            edgecolors='black'
        )
        # Draw its label separately without a bbox
        nx.draw_networkx_labels(
            G,
            pos,
            labels={n: node_labels[n] for n in nodes},
            font_size=10,
            font_weight='bold'
        )
    else: # These are the rectangular nodes
        nx.draw_networkx_labels(
            G,
            pos,
            labels={n: node_labels[n] for n in nodes},
            font_size=10,
            font_weight='bold',
            bbox=dict(
                boxstyle=style_info['style'],
                facecolor=style_info['color'],
                edgecolor='black'
            )
        )

# --- 4. FINALIZE AND SHOW PLOT ---

# Set plot margins to prevent labels from being cut off
plt.margins(0.1)
# Turn off the axes
plt.axis('off')
# Display the graph
plt.show()
