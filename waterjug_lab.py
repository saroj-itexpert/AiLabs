from collections import deque

def water_jug_problem():
    # Initialize the queue for BFS
    queue = deque()
    
    # Start with both jugs empty (X = 0, Y = 0)
    queue.append((0, 0))
    
    # Set to keep track of visited states to avoid repetition
    visited = set()
    
    # List to store the solution steps
    solution_steps = []

    while queue:
        # Get the current state of the jugs
        X, Y = queue.popleft()
        
        # Add the current state to the solution steps
        solution_steps.append((X, Y))
        
        # Check if the current state is the solution
        if X == 2:
            return solution_steps
        
        # If the state has already been visited, skip it
        if (X, Y) in visited:
            continue
        
        # Mark the current state as visited
        visited.add((X, Y))
        
        # Apply the rules/operators
        # 1. Fill X if it's empty
        if X == 0:
            queue.append((4, Y))
        
        # 2. Fill Y if it's empty
        if Y == 0:
            queue.append((X, 3))
        
        # 3. Empty X if it's not empty
        if X > 0:
            queue.append((0, Y))
        
        # 4. Empty Y if it's not empty
        if Y > 0:
            queue.append((X, 0))
        
        # 5. Fill Y from X if possible
        if X + Y >= 3 and X > 0:
            queue.append((X - (3 - Y), 3))
        
        # 6. Fill X from Y if possible
        if X + Y >= 4 and Y > 0:
            queue.append((4, Y - (4 - X)))
        
        # 7. Empty X into Y if possible
        if X + Y <= 3 and X > 0:
            queue.append((0, X + Y))
        
        # 8. Empty Y into X if possible
        if X + Y <= 4 and Y > 0:
            queue.append((X + Y, 0))
    
    # If no solution is found, return None
    return None

# Run the function to find the solution
solution = water_jug_problem()

# Print the solution steps
if solution:
    print("Solution steps:")
    for step in solution:
        print(f"Jug X: {step[0]} gallons, Jug Y: {step[1]} gallons")
else:
    print("No solution found.")
