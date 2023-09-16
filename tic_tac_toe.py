import random

# Initialize the tic-tac-toe board
# Each element corresponds to a position on the board - tic tac toe game have 9 elements
board = [' '] * 9

# Define the winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]               # diagonals
]

# Function to draw the tic-tac-toe board
def draw_board():
    print('-------------')
    for i in range(3):
        print(f'| {board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]} |')
        print('-------------')

# Function to check if any player has won
def check_winner():
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            return board[combination[0]]
    return None

# Function to make a move for the computer player
def make_computer_move():
    available_moves = [i for i in range(9) if board[i] == ' ']
    if not available_moves:
        return
    move = random.choice(available_moves)
    board[move] = 'O'

# Function to make a move for the human player
def make_human_move():
    while True:
        move = input("Enter your move (0-8): ")
        if not move.isdigit() or int(move) < 0 or int(move) > 8 or board[int(move)] != ' ':
            print("Invalid move. Try again.")
        else:
            board[int(move)] = 'X'
            break

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    draw_board()

    while True:
        make_human_move()
        draw_board()
        winner = check_winner()
        if winner:
            print(f"Congratulations! {winner} wins!")
            break

        make_computer_move()
        draw_board()
        winner = check_winner()
        if winner:
            print(f"Sorry! {winner} wins!")
            break

        if ' ' not in board:
            print("It's a tie!")
            break


# Start the game
play_game()
