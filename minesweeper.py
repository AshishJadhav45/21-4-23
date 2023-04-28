import random

# Define the game board size and number of mines
BOARD_SIZE = 10
NUM_MINES = 10

# Create a new game board filled with zeros
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Place mines randomly on the board
for _ in range(NUM_MINES):
    i, j = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
    board[i][j] = '*'

# Define a helper function to count the number of mines around a cell
def count_mines(i, j):
    if board[i][j] == '*':
        return '*'
    count = 0
    for x in range(max(i - 1, 0), min(i + 2, BOARD_SIZE)):
        for y in range(max(j - 1, 0), min(j + 2, BOARD_SIZE)):
            if board[x][y] == '*':
                count += 1
    return count

# Update the game board with the mine counts
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if board[i][j] != '*':
            board[i][j] = count_mines(i, j)

# Define a function to display the game board
def display_board():
    for row in board:
        print(' '.join(str(cell) for cell in row))

# Play the game!
while True:
    display_board()
    i, j = map(int, input('Enter row and column to reveal (e.g. "3 4"): ').split())
    if board[i][j] == '*':
        print('Game over! You hit a mine.')
        break
    board[i][j] = count_mines(i, j)
    if all('*' not in row for row in board):
        print('Congratulations! You won!')
        break
