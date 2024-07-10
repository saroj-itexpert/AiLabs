def bfs(graph, node, goal_node):  # function for BFS
   
    visited = set()  # set for visited nodes so that no any nodes are repeated.
    queue = []  # Initialize a queue

    if node == goal_node:
        return [node]

    visited.add(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        path = queue.pop(0)
        # print '->' after each node except the last one
        print(path, end='->' if path != f'{goal_node}' else '')
        if path == goal_node:
            return path

        for neighbour in graph[path]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
 
    return None



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
print("Following is the Breadth-First Search")
start_node = 'A'
goal_node = 'I'
path = bfs(graph, start_node,goal_node)

if path:
    print(" -> ".join(path))
else:
    print("No path found from {} to {}".format(start_node, goal_node))

