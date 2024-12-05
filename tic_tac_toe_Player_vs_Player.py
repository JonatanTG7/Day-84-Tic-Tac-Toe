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

#printing the borad with the X & O
def print_board():
    print("\nTic_Tac_Toe_Game:\n")

    #Creating the board.
    for index,row in enumerate(board):
        print("  |".join(row))
        if index != 2:
            print("-----------")

#checking if the row and column that the user is entering is corrcet and free.
def player_turn(player):
    valid_move =False
    while not valid_move:
        print(f"\nTurn of {player} :")

        row = input("Please enter a row between 0-2: ")
        column = input("Please enter a column between 0-2: ")

        if row not in row_column_index or column not in row_column_index:
            print(f"Invalid input! Please enter a valid input 0, 1 or 2 to row and column. ")
        elif board[int(row)][int(column)] != " ":
            print("The row and column you enter is not free, try a diffrent place. ")
        else:
            board[int(row)][int(column)] = f"{player}"
            valid_move = True
            print_board()
            
#checking if one of the users won the game.
def check_winner(player,count_turns):
    is_winner = False
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == player:
            is_winner = True
    for j in range(len(board[0])):
        if board[0][j] == board[1][j] == board[2][j] == player:
            is_winner = True

    if all(board[i][i] == player for i in range(3)) or all([board[i][2 - i] == player for i in range(3)]): 
        is_winner = True

    if is_winner:
        print(f"The player {player} won! ")
        return True
    
    if count_turns == 8:
        print("It is a draw :)")
        return True
    return False

#main func 
def start_game():
    print_board()
    winning = False
    count_turns = 0
    current_player = game_turn[randint(0,1)]
    while not winning:
        player_turn(current_player)
        winning = check_winner(current_player,count_turns)
        count_turns += 1
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

start_game()