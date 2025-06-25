import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def create_argumentation_graph():
    """
    Creates and displays a visual representation of the argumentation analysis
    for the "fire drone" fact-check report.
    """
    # 1. Initialize the directed graph
    G = nx.DiGraph()

    # 2. Define nodes with their text labels and types
    # The node ID is the first argument, followed by attributes for label and type.
    
    # B-Objects (to be visualized as blue rectangles)
    G.add_node('aircraft', label='Aircraft', type='b_object')
    G.add_node('action', label='Action: Setting Fires', type='b_object')
    G.add_node('arson', label='Goal: Malicious Arson', type='b_object')
    G.add_node('platforms', label='Tech Platforms', type='b_object')
    G.add_node('video', label='The Video', type='b_object')
    
    # B-Relationships (green rhombuses/diamonds)
    G.add_node('purpose_rel', label='HAS PURPOSE OF', type='b_relationship')
    G.add_node('perform_rel', label='PERFORMED BY', type='b_relationship')
    G.add_node('suppress_rel', label='ALLEGEDLY SUPPRESSING', type='b_relationship')

    # B-Attributes (orange rectangles)
    G.add_node('type_attr', label='CLAIMED TYPE', type='b_attribute')

    # B-Values (yellow rectangles)
    G.add_node('drone_val', label='Drone', type='b_value')

    # Verdicts & Notes (grey rectangles)
    G.add_node('verdict', 
               label='<FALSE RELATIONSHIP>\nFact: Purpose is a controlled burn,\na standard firefighting tactic.', 
               type='verdict')
    G.add_node('note_type', 
               label='Note: The aircraft is a\nhelicopter, not a drone.', 
               type='verdict')
    G.add_node('note_suppress', 
               label='Note: Video is widely available,\nnot suppressed.', 
               type='verdict')

    # 3. Define the connections (edges) between the nodes
    # Connections follow the hierarchy: Object -> Relationship or Object -> Attribute
    G.add_edge('action', 'purpose_rel')
    G.add_edge('purpose_rel', 'arson')
    
    G.add_edge('aircraft', 'perform_rel')
    G.add_edge('perform_rel', 'action')
    
    G.add_edge('aircraft', 'type_attr')
    G.add_edge('type_attr', 'drone_val')
    
    G.add_edge('platforms', 'suppress_rel')
    G.add_edge('suppress_rel', 'video')

    # Connections from Verdicts/Notes to the components they refute
    G.add_edge('verdict', 'purpose_rel')
    G.add_edge('note_type', 'type_attr')
    G.add_edge('note_suppress', 'suppress_rel')

    # 4. Define manual positions for a clear, non-overlapping layout
    pos = {
        'action': (0, 0),
        'perform_rel': (-1.5, 0),
        'aircraft': (-3, 0),
        
        'purpose_rel': (1.5, 0),
        'arson': (3.2, 0),
        
        'type_attr': (-3, 1.2),
        'drone_val': (-3, 2.2),
        
        'platforms': (-1.5, -2),
        'suppress_rel': (0, -2),
        'video': (1.5, -2),
        
        'verdict': (1.5, 1.5),
        'note_type': (-5, 1.2),
        'note_suppress': (0,-3.2),
    }

    # 5. Define colors and shapes based on the 'type' attribute
    color_map = {
        'b_object': '#a3c4f3',       # Blue
        'b_relationship': '#b5e48c', # Green
        'b_attribute': '#fca311',    # Orange
        'b_value': '#ffdd00',        # Yellow
        'verdict': '#adb5bd'         # Grey
    }

    # Separate nodes by their type for drawing with different shapes
    node_lists = {
        'rectangles': [n for n, d in G.nodes(data=True) if d['type'] in ['b_object', 'b_attribute', 'b_value', 'verdict']],
        'rhombus': [n for n, d in G.nodes(data=True) if d['type'] == 'b_relationship']
    }

    # Get colors for each node
    node_colors_rect = [color_map[G.nodes[n]['type']] for n in node_lists['rectangles']]
    node_colors_rhombus = [color_map[G.nodes[n]['type']] for n in node_lists['rhombus']]
    
    # 6. Draw the graph
    plt.figure(figsize=(18, 12))
    plt.title('Argumentation Graph of "Fire Drone" Fact-Check', fontsize=20)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, nodelist=node_lists['rectangles'], node_shape='s', 
                           node_size=6000, node_color=node_colors_rect)
    nx.draw_networkx_nodes(G, pos, nodelist=node_lists['rhombus'], node_shape='D', 
                           node_size=6000, node_color=node_colors_rhombus)

    # Draw edges
    nx.draw_networkx_edges(G, pos, node_size=6000, arrowstyle='->', arrowsize=20, 
                           width=1.5, connectionstyle='arc3,rad=0.1')

    # Draw labels
    labels = {n: d['label'] for n, d in G.nodes(data=True)}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=11, font_family='sans-serif')
    
    # 7. Create a legend to explain the components
    legend_handles = [
        mpatches.Patch(color='#a3c4f3', label='B-Object: An entity or concept'),
        mpatches.Patch(color='#b5e48c', label='B-Relationship: Connects two objects'),
        mpatches.Patch(color='#fca311', label='B-Attribute: A property of an object'),
        mpatches.Patch(color='#ffdd00', label='B-Value: The value of an attribute'),
        mpatches.Patch(color='#adb5bd', label='Verdict/Note: Fact-check finding')
    ]
    plt.legend(handles=legend_handles, loc='lower right', fontsize=12, title='Graph Components')

    # Show the plot
    plt.box(False)
    plt.tight_layout()
    plt.show()

# Execute the function to generate the graph
create_argumentation_graph()
