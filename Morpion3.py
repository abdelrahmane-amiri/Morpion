tableau = [[1,2,3],[4,5,6],[7,8,9]]
Player1= "X"
Player2= "O"
Player_Act = Player1
row =3
column = 3

def check_Win():
    win = False
    if tableau[0][0] == tableau[0][1] == tableau[0][2]:
        win = True
    if tableau[1][0] == tableau[1][1] == tableau[1][2]:
        win = True
    if tableau[2][0] == tableau[2][1] == tableau[2][2]:
        win = True
    if tableau[0][0] == tableau[1][0] == tableau[2][0]:
        win = True
    if tableau[0][1] == tableau[1][1] == tableau[2][1]:
        win = True
    if tableau[0][2] == tableau[1][2] == tableau[2][2]:
        win = True
    if tableau[0][0] == tableau[1][1] == tableau[2][2]:
        win = True
    if tableau[0][2] == tableau[1][1] == tableau[2][0]:
        win = True
    return win
    

def creation():
    for i in range(row):
        print("\n+---+---+---+")
        print("|", end="")
        for j in range(column):
            print("", tableau[i][j], end=" |")

    print("\n+---+---+---+")

def Saisie():
    global Player_Act
    click = int(input("Au " + Player_Act + " de joueur: "))
    
    if 1 <= click <= 9:
            row = (click - 1) // 3
            col = (click - 1) % 3 
            if tableau[row][col] != "X" and "O":
                tableau[row][col] = Player_Act

                if Player_Act == Player1:
                    Player_Act = Player2
                else: Player_Act = Player1

    else: print("Saisi un nombre en 1 et 9 ")
             

        
while check_Win() == False: 
    creation()
    Saisie()
    creation()

if Player_Act == Player1:
            Player_Act = Player2
else: Player_Act = Player1
print(Player_Act," a gagner")