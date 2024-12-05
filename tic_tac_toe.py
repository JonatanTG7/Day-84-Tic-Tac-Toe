#Tic_Tac_Toe_Game
#Player vs Player

from random import randint

#board matrix 3x3
board = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
]

#Player symbols 
game_turn =["X" , "O"]

#Number of rows and columns
row_column_index =["0" ,"1", "2"]

#
def print_board():
    print("\nTic_Tac_Toe_Game:\n")

    #Creating the board
    for index,row in enumerate(board):
        print("  |".join(row))
        if index != 2:
            print("-----------")
     
def player_turn(player):
    valid_move =False
    while not valid_move:
        print(f"\nTurn of {player} :")
        row = input("Please enter a row between 0-2: ")
        column = input("Please enter a column between 0-2: ")
        if row not in row_column_index:
            print(f"You entered {row} and this is wrong. enter 0, 1 or 2")
        elif column not in row_column_index:
            print(f"You entered {column} and this is wrong. enter 0, 1 or 2")
        elif board[int(row)][int(column)] != " ":
            print("The row and column you enter is not free, try a diffrent place ")
        else:
            board[int(row)][int(column)] = f"{player}"
            print_board()
            valid_move = True
            

def check_winner(player,game_draw):
    print_message = False
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][2] != " ":
            print_message = True
    for j in range(len(board[0])):
        if board[0][j] == board[1][j] == board[2][j] and board[2][j] != " ":
            print_message = True
    if board[0][0] == board[1][1] == board[2][2] and board[2][2] != " ":
            print_message = True
    if board[2][0] == board[1][1] == board[0][2] and board[0][2] != " ":
            print_message = True
    if print_message:
        print(f"The player {player} won! ")
        return True
    if game_draw == 8:
        print("It is a draw :)")
        return True
    return False
        
def game():
    print_board()
    winning = False
    game_draw = 0
    current_player = game_turn[randint(0,1)]
    while not winning:
        player_turn(current_player)
        winning = check_winner(current_player,game_draw)
        game_draw += 1
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

game()