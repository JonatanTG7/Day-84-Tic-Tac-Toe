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

#Printing the borad with the X & O
def print_board():
    print("\nTic_Tac_Toe_Game:\n")

    #Creating the board.
    for index,row in enumerate(board):
        print("  |".join(row))
        if index != 2:
            print("-----------")

#Checking if the row and column that the user is entering is correct and free.
def player_turn(player):
    valid_move =False
    while not valid_move:
        print(f"\nTurn of {player} :")

        #Input from user
        row = input("Please enter a row between 0-2: ")
        column = input("Please enter a column between 0-2: ")

        #Checks if the input is valid (0 , 1 or 2)
        if row not in row_column_index or column not in row_column_index:
            print(f"Invalid input! Please enter a valid input 0, 1 or 2 to row and column. ")
        #Checks if the cell is free
        elif board[int(row)][int(column)] != " ":
            print("The row and column you enter is not free, try a diffrent place. ")
        else:
            #Add the symbol of the player to the board
            board[int(row)][int(column)] = f"{player}"
            valid_move = True
            print_board()
            
#Checking if one of the users won the game.
def check_winner(player,count_turns):
    is_winner = False
    #Checks if we have a same symbol in the row
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == player:
            is_winner = True
    #Checks if we have a same symbol in the column
    for j in range(len(board[0])):
        if board[0][j] == board[1][j] == board[2][j] == player:
            is_winner = True

    #Checks if we have a same symbol in the diagonal
    if all(board[i][i] == player for i in range(3)) or all([board[i][2 - i] == player for i in range(3)]): 
        is_winner = True

    #Checks if I won
    if is_winner:
        print(f"The player {player} won! ")
        return True
    
    #Checks if draw after 9 moves
    if count_turns == 9:
        print("It is a draw :)")
        return True
    return False

#Main func 
def start_game():

    #Printing the board before starting
    print_board()

    #For while loop
    winning = False
    #Couning moves
    count_turns = 1
    #Random player start
    current_player = game_turn[randint(0,1)]
    #While until win or draw
    while not winning:
        #Player turn
        player_turn(current_player)
        #Checks if we have a winner
        if count_turns <= 5:
            winning = check_winner(current_player,count_turns)
        #move ++
        count_turns += 1

        #Changing player turn
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

start_game()