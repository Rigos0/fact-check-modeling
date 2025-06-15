from e2b_code_interpreter import Sandbox
import base64

code = """
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def visualize_argumentation():
    # 1. Build the Graph
    G = nx.DiGraph()

    # Add nodes with attributes for type and label
    # B-objects
    G.add_node("biden", type="b-object", label="Joe Biden")
    G.add_node("sanders", type="b-object", label="Bernie Sanders")
    G.add_node("policies", type="b-object", label="Policy Stances")

    # B-relationship
    G.add_node("similar", type="b-relationship", label="is similar to")

    # Verdict
    G.add_node("verdict", type="verdict", label="EXAGGERATED SIMILARITY")

    # Add edges with labels to define the relationships
    G.add_edge("similar", "biden", label="subject")
    G.add_edge("similar", "sanders", label="object")
    G.add_edge("similar", "policies", label="on")
    G.add_edge("verdict", "similar", label="points to")

    # 2. Visualize the Graph

    # Define visual properties based on node type
    node_colors_map = {
        "b-object": "skyblue",
        "b-relationship": "lightgreen",
        "verdict": "lightgrey"
    }
    node_shapes_map = {
        "b-object": "s",  # square for rectangle
        "b-relationship": "D",  # diamond
        "verdict": "s"    # square for rectangle
    }

    # Prepare lists of nodes for each type to draw them separately
    node_types = {
        "b-object": [],
        "b-relationship": [],
        "verdict": []
    }
    for node, data in G.nodes(data=True):
        node_types[data['type']].append(node)

    # Use a spring layout for better node spacing
    # A seed ensures the layout is reproducible
    # k adjusts the optimal distance between nodes
    pos = nx.spring_layout(G, seed=42, k=1.8)

    # Create the plot
    plt.figure(figsize=(12, 9))
    ax = plt.gca()
    ax.set_title("Argumentation Graph: 'No Daylight' Between Biden and Sanders", fontsize=16)

    # Draw each node type with its specific shape and color
    for n_type, nodes in node_types.items():
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=nodes,
            node_size=4000,
            node_color=node_colors_map[n_type],
            node_shape=node_shapes_map[n_type],
            edgecolors="black"
        )

    # Draw edges (arrows)
    nx.draw_networkx_edges(
        G,
        pos,
        node_size=4000,
        arrowstyle="->",
        arrowsize=20,
        edge_color="gray",
        width=1.5
    )

    # Draw node labels
    node_labels = {node: data['label'] for node, data in G.nodes(data=True)}
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_weight="bold")

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color='darkred')

    # Create a legend
    legend_patches = [
        mpatches.Patch(color='skyblue', label='B-object'),
        mpatches.Patch(color='lightgreen', label='B-relationship'),
        mpatches.Patch(color='lightgrey', label='Verdict')
    ]
    plt.legend(handles=legend_patches, loc='upper right', fontsize=10)

    # Display the graph
    plt.axis('off')
    plt.tight_layout()
    plt.show()

visualize_argumentation()
"""

sandbox = Sandbox()
sandbox.commands.run("pip install networkx")
execution = sandbox.run_code(code)

# There's only one result in this case - the plot displayed with `plt.show()`
first_result = execution.results[0]

if first_result.png:
  # Save the png to a file. The png is in base64 format.
  with open('chart.png', 'wb') as f:
    f.write(base64.b64decode(first_result.png))
  print('Chart saved as chart.png')

