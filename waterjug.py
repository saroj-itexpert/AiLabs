'''
Program to solve the water jug problem using state space search
'''

j1 = 0
j2 = 0
x = 4
y = 3
print("Initial state: (0, 0)")
print("Capacities: (4, 3)")
print("Goal state: (2, 0 or any number)")

while j1 != 2:
    print("Choose a rule to apply:")
    print("1: Fill Jug X (if X is 0)")
    print("2: Fill Jug Y (if Y is 0)")
    print("3: Empty Jug X (if X > 0)")
    print("4: Empty Jug Y (if Y > 0)")
    print("5: Fill Jug Y from Jug X (if X + Y >= 3 and X > 0)")
    print("6: Fill Jug X from Jug Y (if X + Y >= 4 and Y > 0)")
    print("7: Empty Jug X into Jug Y (if X + Y <= 3 and X > 0)")
    print("8: Empty Jug Y into Jug X (if X + Y <= 4 and Y > 0)")
    r = int(input("Enter the rule: "))
    if (r == 1):
        j1 = x
    elif (r == 2):
        j2 = y
    elif (r == 3):
        j1 = 0
    elif (r == 4):
        j2 = 0
    elif (r == 5):
        t = y-j2
        j2 = y
        j1 -= t
        if j1 < 0:
            j1 = 0
    elif (r == 6):
        t = x-j1
        j1 = x
        j2 -= t
        if j2 < 0:
            j2 = 0
    elif (r == 7):
        j2 += j1
        j1 = 0
        if j2 > y:
            j2 = y
    elif (r == 8):
        j1 += j2
        j2 = 0
        if j1 > x:
            j1 = x
    print(j1, j2)