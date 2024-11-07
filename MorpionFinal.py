
import random
#function for setup game
def game():
    global tableau, Player_Act, win, draw, Player1, Player2,row,column,mode
    tableau = [[" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "]]
    Player1 = "X"
    Player2 = "O"
    Player_Act = Player1 
    win = False
    draw = False
    row = 3
    column= 3

    #Choose play
    mode = input("Choisir le mode de jeu: 1 = Joueur Vs Joueur; 2 = Joueur Vs Ia: ")

#function for Ia
def ia():
    global tableau
    global check_row
    global check_column
    global disponible
    global alea

    #verify win
    for row in range(3):
        if tableau[row][0] == tableau[row][1] == "O" and tableau[row][2] == " ":
            return (row, 2)
        if tableau[row][1] == tableau[row][2] == "O" and tableau[row][0] == " ":
            return (row, 0)
        if tableau[row][0] == tableau[row][2] == "O" and tableau[row][1] == " ":
            return (row, 1)
        
    for column in range(3):
        if tableau[0][column] == tableau[1][column] == "O" and tableau[2][column] == " ":
            return (2, column)
        if tableau[1][column] == tableau[2][column] == "O" and tableau[0][column] == " ":
            return (0, column)
        if tableau[0][column] == tableau[2][column] == "O" and tableau[1][column] == " ":
            return (1, column)
        
    #verify if player1 not win
    for row in range(3):
        if tableau[row][0] == tableau[row][1] == "X" and tableau[row][2] == " ":
            return (row, 2)
        if tableau[row][1] == tableau[row][2] == "X" and tableau[row][0] == " ":
            return (row, 0)
        if tableau[row][0] == tableau[row][2] == "X" and tableau[row][1] == " ":
            return (row, 1)
        
    for column in range(3):
        if tableau[0][column] == tableau[1][column] == "X" and tableau[2][column] == " ":
            return (2, column)
        if tableau[1][column] == tableau[2][column] == "X" and tableau[0][column] == " ":
            return (0, column)
        if tableau[0][column] == tableau[2][column] == "X" and tableau[1][column] == " ":
            return (1, column)
    
    #Diagonal block player
    if tableau[0][0] == tableau[1][1] == "X" and tableau[2][2] == " ":
        return (2, 2)
    if tableau[2][2] == tableau[1][1] == "X" and tableau[0][0] == " ":
        return (0, 0)
    if tableau[0][0] == tableau[2][2] == "X" and tableau[1][1] == " ":
        return (1, 1)
    
    if tableau[0][2] == tableau[1][1] == "X" and tableau[2][0] == " ":
        return (2, 0)
    if tableau[2][0] == tableau[1][1] == "X" and tableau[0][2] == " ":
        return (0, 2)
    if tableau[2][0] == tableau[0][2] == "X" and tableau[1][1] == " ":
        return (1, 1)
    

    #Diagonal win if he can
    if tableau[0][0] == tableau[1][1] == "O" and tableau[2][2] == " ":
        return (2, 2)
    if tableau[2][2] == tableau[1][1] == "O" and tableau[0][0] == " ":
        return (0, 0)
    if tableau[0][0] == tableau[2][2] == "O" and tableau[1][1] == " ":
        return (1, 1)
    
    if tableau[0][2] == tableau[1][1] == "O" and tableau[2][0] == " ":
        return (2, 0)
    if tableau[2][0] == tableau[1][1] == "O" and tableau[0][2] == " ":
        return (0, 2)
    if tableau[2][0] == tableau[0][2] == "O" and tableau[1][1] == " ":
        return (1, 1)


    #if not win for ia or player play random disponible case
    disponible = []
    for row in range(3):
        for column in range(3): 
            if tableau[row][column] == " ":
                disponible.append((row, column)) 

        if disponible:
             alea = random.randint(0, len(disponible) - 1)
             return disponible[alea]

#function for check if a player win
def check_Win():
    global win, draw
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
    if mode == "1" or Player_Act == Player1:
        click = int(input("Au " + Player_Act + " de joueur: "))
        
        if 1 <= click <= 9:

                row = (click - 1) // 3
                col = (click - 1) % 3 
                if tableau[row][col] != Player1 and tableau[row][col] != Player2:
                    tableau[row][col] = Player_Act
                    change_player()

        else: print("Saisi un nombre en 1 et 9 : ")
    elif mode == "2" and Player_Act == Player2:
       r, c = ia()
       tableau[r][c] = Player_Act
       change_player()

#function for change Player Actual
def change_player():
    global Player_Act
    if Player_Act == Player1:
            Player_Act = Player2
    else: Player_Act = Player1


             
#end game  
while True:
    game()
    creation()       
    while check_Win() == False and draw ==False : 
        input_symbols()
        creation()

    #Win or Draw
    if win == True:
        change_player()
        print(f"{Player_Act} a gagner")
    else:
        print("Match nul")

    #Restart
    restart = (input("Enter 'R' pour Recommencer, 'Autre touche' pour sortir: "))
    if restart != "R" and restart != "r":
        print("Partie Terminer")
        break
    
