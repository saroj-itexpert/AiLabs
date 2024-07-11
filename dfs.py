visited = set()  #Define a visited set which takes unique items in it

#Recursive method to iterate through method
def dfs(visited, graph, node):              #dfs method which takes in visited, graph and node as parameter
    if node not in visited:                 #checks if the node is already in the visited set or not
        print(node)                         #print the path with the nodes
        visited.add(node)                   #if not in visited node then add the current node in visisted set.
        for neighbour in graph[node]:       #for loop to traverse through each node's childs in graph dictionary
            dfs(visited, graph, neighbour)  #recursion function to again call the dfs method to traverse the graph.


# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

print("Following is the Depth-First Search")
dfs(visited, graph, '5')