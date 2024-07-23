# Define the initial empty board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Check for winner
def check_winner(board, player):
    for row in board:
        if all(spot == player for spot in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Check if the board is full
def is_full(board):
    return all(spot != ' ' for row in board for spot in row)

# Evaluate the board for the current player
def evaluate(board):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    return 0

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 1:
        return score - depth
    if score == -1:
        return score + depth
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best_score

# Find the best move
def find_best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main function to simulate the game
def main():
    board = initialize_board()
    print("Initial board:")
    for row in board:
        print(row)

    player = 'X'  # X is the maximizer
    opponent = 'O'  # O is the minimizer

    # Example of finding the best move
    best_move = find_best_move(board)
    print("\nBest move for 'X':", best_move)

if __name__ == "__main__":
    main()
