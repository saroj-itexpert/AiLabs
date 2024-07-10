def bfs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    queue = [[start]]  # Initialize the queue with the start node in a list

    if start == goal:
        return [start]

    while queue:
        # Get the first path from the queue
        path = queue.pop(0)
        # Get the last node from the path
        node = path[-1]

        if node not in visited:
            # Mark the node as visited
            visited.add(node)

            # Enumerate all adjacent nodes, construct a new path and push it into the queue
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                # Return path if neighbor is the goal
                if neighbor == goal:
                    return new_path

    # Return None if no path is found
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

# Driver code
start_node = 'A'
goal_node = 'Z'
print("Following is the Breadth-First Search path from {} to {}:".format(start_node, goal_node))
path = bfs(graph, start_node, goal_node)

if path:
    print(" -> ".join(path))
else:
    print("No path found from {} to {}".format(start_node, goal_node))
