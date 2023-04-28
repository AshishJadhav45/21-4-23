# first we create board using define board using Print_board function

def print_board(board):
    print("  |  |")
    print(" "+board[0]+"| "+board[1]+"| "+board[2])
    print("  |  |")
    print("--|--|--")
    print("  |  |")
    print(" "+board[3]+"| "+board[4]+"| "+board[5])
    print("  |  |")
    print("--|--|--")
    print("  |  |")
    print(" "+board[6]+"| "+board[7]+"| "+board[8])


''' This is a Python function named check_win that takes two arguments: a list representing the current state of a tic-tac-toe board and a string representing the symbol (X or O) of the player whose win status is being checked.

The function checks if the player has won the game by examining the board for any three consecutive cells in the same row, column, or diagonal that are marked by the player's symbol. If such a pattern is found, the function returns True, indicating that the player has won. Otherwise, it returns False. '''

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2]==player) or \
       (board[3] == player and board[4] == player and board[5]==player) or \
       (board[6] == player and board[7] == player and board[8]==player) or \
       (board[0] == player and board[3] == player and board[6]==player) or \
       (board[1] == player and board[4] == player and board[7]==player) or \
       (board[2] == player and board[5] == player and board[8]==player) or \
       (board[0] == player and board[4] == player and board[8]==player) or \
       (board[2] == player and board[4] == player and board[6]==player):
       return True
    else:
        return False

# This is a Python function named tic_tac_toe() that initializes the variables used in a game of tic-tac-toe.
def tic_tac_toe():
    board = [" "," "," "," "," "," "," "," "," "]
    player = ["X" , "O"]
    current_player = player[0]
    win = False

# the conditions 
    while not win:
        print_board(board)
        print("it's " + current_player + "'s turn.")

        move = int(input("Enter a number between 1 and 9: ")) -1
        if board[move] == " ":
            board[move] = current_player
        else:
            print("Thats space already taken. Try again.")
            continue
        
        if check_win(board, current_player):
            print_board(board)
            print(current_player + "wins!")
            win = True
        elif " " not in board:
            print_board(board)
            print("It's a tie!")
            break
        else:
            current_player = player[(player.index(current_player) + 1) % 2] 
# finaly we call a function
tic_tac_toe()             

        