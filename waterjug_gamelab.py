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

def play_water_jug_game():
    state = (0, 0)  # Start with both jugs empty
    visited_states = set()  # Track visited states
    path = []  # Track the path of states

    print("Water Jug Game: Goal is to have exactly 2 gallons in Jug X (4-gallon jug).")

    while True:
        print(f"\nCurrent State: Jug X: {state[0]} gallons, Jug Y: {state[1]} gallons")

        if state[0] == 2:
            print("Congratulations! You've solved the problem.")
            path.append(state)
            break

        visited_states.add(state)
        path.append(state)

        print("Choose a rule to apply:")
        print("1: Fill Jug X (if X is 0)")
        print("2: Fill Jug Y (if Y is 0)")
        print("3: Empty Jug X (if X > 0)")
        print("4: Empty Jug Y (if Y > 0)")
        print("5: Fill Jug Y from Jug X (if X + Y >= 3 and X > 0)")
        print("6: Fill Jug X from Jug Y (if X + Y >= 4 and Y > 0)")
        print("7: Empty Jug X into Jug Y (if X + Y <= 3 and X > 0)")
        print("8: Empty Jug Y into Jug X (if X + Y <= 4 and Y > 0)")
        
        try:
            rule = int(input("Enter rule number (1-8): "))
            if rule < 1 or rule > 8:
                print("Invalid rule number. Please enter a number between 1 and 8.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue

        new_state = apply_rule(state, rule)

        if new_state is None:
            print("Rule cannot be applied to the current state.")
        elif new_state in visited_states:
            print("This state has already been visited.")
        else:
            state = new_state

    print("\nSolution Path:")
    for step in path:
        print(f"Jug X: {step[0]} gallons, Jug Y: {step[1]} gallons")

play_water_jug_game()
