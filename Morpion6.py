
#Setup for game
tableau = [[" "," "," "],
           [" "," "," "],
           [" "," "," "]]
Player1= "X"
Player2= "O"
Player_Act = Player1
row =3
column = 3
win = False
draw = False


#function for check if a player win
def check_Win():
    global win
    global draw
    for row in range (3):#verify if win in all row
         if tableau[row][0] == tableau[row][1] == tableau[row][2] != " ":
              win = True
              

    for column in range (3):#verify if win in all column
         if tableau[0][column] == tableau[1][column] == tableau[2][column] != " ":
              win = True

    #verify diagonals
    if tableau[0][0] == tableau[1][1] == tableau[2][2] != " ":
        win = True
    if tableau[0][2] == tableau[1][1] == tableau[2][0] != " ":
        win = True

    #verify draw
    if       tableau[0][0] != " " and tableau[0][1] != " " and tableau[0][2] != " " and \
             tableau[1][0] != " " and tableau[1][1] != " " and tableau[1][2] != " " and \
             tableau[2][0] != " " and tableau[2][1] != " " and tableau[2][2] != " ":
    
        draw = True

    return win
    
#function for create a board
def creation():
    for i in range(row):
        print("\n+---+---+---+")
        print("|", end="")
        for j in range(column):
            print("", tableau[i][j], end=" |")

    print("\n+---+---+---+")

#function for entering symbols
def input_symbols():
    global Player_Act
    click = int(input("Au " + Player_Act + " de joueur: "))
    
    if 1 <= click <= 9:

            row = (click - 1) // 3
            col = (click - 1) % 3 
            if tableau[row][col] != Player1 and tableau[row][col] != Player2:
                tableau[row][col] = Player_Act
                change_player()

    else: print("Saisi un nombre en 1 et 9 ")

#function for change Player Actual
def change_player():
    global Player_Act
    if Player_Act == Player1:
            Player_Act = Player2
    else: Player_Act = Player1
             
#end game
creation()       
while check_Win() == False and draw ==False : 
    input_symbols()
    creation()

if win == True:
    change_player()
    print(Player_Act," a gagner")
else:
     print("Match nul")
