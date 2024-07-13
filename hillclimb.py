import random
import copy

class SlidingPuzzle:
    def __init__(self, initial_state):
        self.state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def is_goal(self, state):
        return state == self.goal_state

    def get_possible_moves(self, state):
        moves = []
        x, y = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
        if x > 0: moves.append((x - 1, y))
        if x < 2: moves.append((x + 1, y))
        if y > 0: moves.append((x, y - 1))
        if y < 2: moves.append((x, y + 1))
        return moves

    def apply_move(self, state, move):
        new_state = copy.deepcopy(state)
        x, y = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
        new_x, new_y = move
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
        return new_state

    def heuristic_misplaced_tiles(self, state):
        misplaced = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0 and state[i][j] != self.goal_state[i][j]:
                    misplaced += 1
        return misplaced

    def heuristic_manhattan_distance(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    x, y = divmod(state[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def hill_climb(self, heuristic):
        current_state = self.state
        steps = 0
        while not self.is_goal(current_state):
            next_states = [self.apply_move(current_state, move) for move in self.get_possible_moves(current_state)]
            next_state = min(next_states, key=heuristic)
            if heuristic(next_state) >= heuristic(current_state):
                break
            current_state = next_state
            steps += 1
            print(f"Step {steps}:")
            for row in current_state:
                print(row)
            print(f"Heuristic Value: {heuristic(current_state)}\n")
        return current_state

# Initial state of the puzzle
initial_state = [
    [1, 2, 3],
    [4, 7, 6],
    [5, 0, 8]
]

puzzle = SlidingPuzzle(initial_state)

print("Solving using Misplaced Tiles Heuristic:")
puzzle.hill_climb(puzzle.heuristic_misplaced_tiles)

print("\nSolving using Manhattan Distance Heuristic:")
puzzle.hill_climb(puzzle.heuristic_manhattan_distance)
