def bfs(graph, start_node, goal_node):  # function for BFS
   
    visited = set()  # set for visited nodes so that no any nodes are repeated.
    queue = []  # Initialize a queue

    if start_node == goal_node:
        return [start_node]
    
    visited.add(start_node)
    queue.append(start_node)
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
start_node = 'A'
goal_node = 'D'
print("Following is the Breadth-First Search path:")
bfs(graph, start_node,goal_node)

