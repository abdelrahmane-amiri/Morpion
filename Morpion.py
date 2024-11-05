nombre = [1,2,3,4,5,6,7,8,9]
tableau = [[1,2,3],[4,5,6],[7,8,9]]
row =3
column = 3

def creation():
    for i in range(row):
        print("\n+---+---+---+")
        print("|", end="")
        for j in range(column):
            print("", tableau[i][j], end=" |")

    print("\n+---+---+---+")
        

creation()