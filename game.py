# create the game board
board = ["  " for i in range(9)]

#function to display the game board
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):

    # determine player order
    if icon == "X":
        number = 1
    if icon == "O":
        number = 2
        
    print("Your turn player {}: ".format(number))
    #get user input
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == "  ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")

#check for victory
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

#check for draw
def is_draw():
    if "  " not in board:
        return True
    else:
        return False

#Game loop logic
while True:
    print_board()
    player_move("X")
    print_board()
    # check if X wins or game is a draw
    if is_victory("X"):
        print("X Wins!  Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    # check if O wins or game is a draw
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins!  Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break

