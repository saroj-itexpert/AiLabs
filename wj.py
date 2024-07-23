def apply_rule(state, rule):
    X, Y = state
    if rule == 1:  # Rule 1: If X = 0 then X = 4 (fill X)
        if X == 0:
            return (4, Y)
    elif rule == 2:  # Rule 2: If Y = 0 then Y = 3 (fill Y)
        if Y == 0:
            return (X, 3)
    elif rule == 3:  # Rule 3: If X > 0 then X = 0 (empty X)
        if X > 0:
            return (0, Y)
    elif rule == 4:  # Rule 4: If Y > 0 then Y = 0 (empty Y)
        if Y > 0:
            return (X, 0)
    elif rule == 5:  # Rule 5: If X + Y >= 3 and X > 0 then X = X – (3 – Y) and Y = 3 (fill Y from X)
        if X + Y >= 3 and X > 0:
            return (X - (3 - Y), 3)
    elif rule == 6:  # Rule 6: If X + Y >= 4 and Y > 0 then X = 4 and Y = Y – (4 – X) (fill X from Y)
        if X + Y >= 4 and Y > 0:
            return (4, Y - (4 - X))
    elif rule == 7:  # Rule 7: If X + Y <= 3 and X > 0 then X = 0 and Y = X + Y (empty X into Y)
        if X + Y <= 3 and X > 0:
            return (0, X + Y)
    elif rule == 8:  # Rule 8: If X + Y <= 4 and Y > 0 then X = X + Y and Y = 0 (empty Y into X)
        if X + Y <= 4 and Y > 0:
            return (X + Y, 0)
    return None

def solve_water_jug():
    # Start with both jugs empty
    initial_state = (0, 0)
    # List of rules to apply
    rules = [1, 2, 3, 4, 5, 6, 7, 8]
    # Keep track of the states we visit
    visited_states = set()
    # Queue to keep track of states to explore
    queue = [initial_state]
    # Keep track of the solution path
    path = []

    while queue:
        state = queue.pop(0)  # Get the first state from the queue
        if state[0] == 2:  # If the first jug has exactly 2 gallons, we found a solution
            path.append(state)
            break
        # If we have already visited this state, skip it
        if state in visited_states:
            continue
        visited_states.add(state)  # Mark this state as visited
        path.append(state)  # Add this state to the solution path
        # Try applying each rule to the current state
        for rule in rules:
            new_state = apply_rule(state, rule)
            if new_state and new_state not in visited_states:
                queue.append(new_state)

    return path

# Run the solver and print the solution path
solution_path = solve_water_jug()
print("Solution path:")
for state in solution_path:
    print(f"Jug X: {state[0]} gallons, Jug Y: {state[1]} gallons")
