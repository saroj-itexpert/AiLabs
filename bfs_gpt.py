from collections import deque

def bfs(graph, start, goal):
    # Set for visited nodes to avoid revisiting
    visited = set()
    # Queue for BFS
    queue = deque([start])
    # Track the path using a parent dictionary
    parent = {start: None}
    
    visited.add(start)

    while queue:
        # Dequeue a vertex from the queue
        node = queue.popleft()

        # If the goal is reached, reconstruct and return the path
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path

        # Visit all the neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = node
    
    # If the goal node is not reachable
    return None

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

# Driver Code
start_node = 'A'
goal_node = 'G'
print("Following is the Breadth-First Search path from {} to {}:".format(start_node, goal_node))
path = bfs(graph, start_node, goal_node)

if path:
    print(" -> ".join(path))
else:
    print("No path found from {} to {}".format(start_node, goal_node))
