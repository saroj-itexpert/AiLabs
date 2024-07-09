import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def bfs_visualized(graph, start, goal):
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}
    
    fig, ax = plt.subplots()
    
    pos = nx.spring_layout(graph)  # Positions for all nodes
    
    def draw_graph():
        ax.clear()
        nx.draw(graph, pos, with_labels=True, node_color=['lightblue' if node not in visited else 'lightgreen' for node in graph.nodes], ax=ax)
        plt.pause(0.5)
    
    draw_graph()  # Initial graph
    
    while queue:
        current = queue.popleft()
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current
                draw_graph()  # Update graph each step
    
    return None

# Define the graph using NetworkX
G = nx.Graph()
edges = [
    ('S', 'A'), ('S', 'B'), ('S', 'C'),
    ('A', 'D'), ('A', 'E'),
    ('B', 'F'),
    ('C', 'G'),
    ('E', 'H'),
    ('G', 'I'), ('G', 'K')
]

G.add_edges_from(edges)

# Define start and goal nodes
start = 'S'
goal = 'K'

# Run BFS with visualization
path = bfs_visualized(G, start, goal)

if path:
    print(f"Path from {start} to {goal}: {' -> '.join(path)}")
else:
    print(f"No path found from {start} to {goal}")

plt.show()  # Keep the final graph on screen
