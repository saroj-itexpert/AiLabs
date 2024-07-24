j1 = 0  # Jug X
j2 = 0  # Jug Y
x = 4   # Capacity of Jug X
y = 3   # Capacity of Jug Y

print("Initial state: (0, 0)")
print("Capacities: (4, 3)")
print("Goal state: (2, 0 or any number)")

while j1 != 2:
    print("Choose a rule to apply:")
    print("1: Fill Jug X (if X is not full)")
    print("2: Fill Jug Y (if Y is not full)")
    print("3: Empty Jug X (if X > 0)")
    print("4: Empty Jug Y (if Y > 0)")
    print("5: Fill Jug Y from Jug X (if X + Y >= 3 and X > 0)")
    print("6: Fill Jug X from Jug Y (if X + Y >= 4 and Y > 0)")
    print("7: Empty Jug X into Jug Y (if X + Y <= 3 and X > 0)")
    print("8: Empty Jug Y into Jug X (if X + Y <= 4 and Y > 0)")
    r = int(input("Enter the rule: "))

    if r == 1:
        j1 = x  # Fill Jug 1 to its capacity
    elif r == 2:
        j2 = y  # Fill Jug 2 to its capacity
    elif r == 3:
        j1 = 0  # Empty Jug1
    elif r == 4:
        j2 = 0  # Empty Jug2
    elif r == 5 and j1 + j2 >= y and j1 > 0:
        amount_to_pour = y - j2
        j2 = y  # Fill Jug2 to its capacity
        j1 = j1- amount_to_pour  # Reduce Jug1 by the amount poured into Jug2
        if j1 < 0:  #if value of jug1 becomes negative we put it as 0.
            j1 = 0
    elif r == 6 and j1 + j2 >= x and j2 > 0:
        amount_to_pour = x - j1
        j1 = x  # Fill Jug1 to its capacity
        j2 = j2 - amount_to_pour  # Reduce Jug2 by the amount poured into Jug1
        if j2 < 0:
            j2 = 0
    elif r == 7 and j1 + j2 <= y and j1 > 0:
        j2 = j2 + j1  # Pour all of Jug1 into Jug2
        j1 = 0
        if j2 > y:
            j2 = y
    elif r == 8 and j1 + j2 <= x and j2 > 0:
        j1 = j1 + j2  # Pour all of Jug2 into Jug1
        j2 = 0
        if j1 > x:
            j1 = x

    print(f"Current state: ({j1}, {j2})")

print("Goal achieved!")
