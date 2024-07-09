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

visited = set()  # set for visited nodes so that no any nodes are repeated.
queue = []  # Initialize a queue


def bfs(graph, node):  # function for BFS
    visited.add(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        # print '->' after each node except the last one
        print(m, end='->' if m != 'I' else '')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Driver Code
print("Following is the Breadth-First Search")
bfs(graph, 'A')