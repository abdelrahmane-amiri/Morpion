tableau = [[1,2,3],[4,5,6],[7,8,9]]
Player1= "X"
Player2= "O"
Player_Act = Player1
row =3
column = 3

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
         tableau[row][col] = Player_Act

         if Player_Act == Player1:
            Player_Act = Player2
         else: Player_Act = Player1

    else: print("Saisi un nombre en 1 et 9 ")
             
        
x=0

        
while x !=10:
    creation()
    Saisie()
    creation()