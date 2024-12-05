#Tic_Tac_Toe_Game
#Player vs Player

#borad matrix 3x3
from random import randint


borad = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
]

game_turn =["X" , "O"]

row_column_index =["0" ,"1", "2"]

def create_borad():
    print("Tic_Tac_Toe_Game:\n\n")

    #Creating the board
    for index,row in enumerate(borad):
        print("  |".join(row))
        if index != 2:
            print("-----------")
     
def turn(first):
    print(f"{first} Turn:")
    row = input("enter a row (0,1,2): ")
    column = input("enter a column (0,1,2): ")
    if row not in row_column_index:
        print(f"You enter a wrong row: {row}. enter 0, 1 or 2")
        turn(first)
    elif column not in row_column_index:
        print(f"You enter a wrong column: {column}. enter 0, 1 or 2")
        turn(first)
    elif borad[int(row)][int(column)] == " ":
        borad[int(row)][int(column)] = f"{first}"
        create_borad()
    else:
        print("This place is not free, try again")
        turn(first)

def check_winning(first_start,):
    for i in range(len(borad)):
        if borad[i][0] == borad[i][1] == borad[i][2] and borad[i][2] != " ":
            print(f"You won {first_start}")
            return True
    for j in range(len(borad[0])):
        if borad[0][j] == borad[1][j] == borad[2][j] and borad[2][j] != " ":
            print(f"You won {first_start}")
            return True
    if borad[0][0] == borad[1][1] == borad[2][2] and borad[2][2] != " ":
        print(f"You won {first_start}")
        return True
    if borad[2][0] == borad[1][1] == borad[0][2] and borad[0][2] != " ":
        print(f"You won {first_start}") 
        return True
    return False
        
def game():
    create_borad()
    winning = False
    first_start = game_turn[randint(0,1)]
    while not winning:
        turn(first_start)
        winning = check_winning(first_start)

        if first_start == "X":
            first_start = "O"
        else:
            first_start = "X"
        


    

game()