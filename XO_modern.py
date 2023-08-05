print("Hello! Welcome to Shahroodi's game!")
print("it's version 2 of XO game")
print("\n")
print("Rules: Player 1 and player 2, represented by X and O, take turns "
"marking the spaces in a 3*3 grid. The player who succeeds in placing ")
print("\n")
input("Press enter to continue.")
print("\n")
# Start code
# ----------
A = [[0]*3 for i in range(3)]

def init_table(A):
    home = 1
    for i in range(3):
        for j in range(3):
            A[i][j] = home
            home+=1
def print_table(A):
    print("+---+---+---+")
    for i in range(3):
        for j in range(3):
            print("|", A[i][j] , end= " ")
        print("|",end= " ")
        print()
        print("+---+---+---+")
    print()

def put_number(T,R):
    row = T // 3
    column = T % 3
    A[row][column] = R

def Chek_win(R):
    for i in range(3):
        if A[i][0] == R and A[i][1] == R and A[i][2] == R:
            return True
        if A[0][i] == R and A[1][i] == R and A[2][i] == R:
            return True
    if A[0][0] == R and A[1][1] == R and A[2][2] == R:
        return True
    if A[0][2] == R and A[1][1] == R and A[2][0] == R:
        return True
    return False

init_table(A)
for move_number in range(9):

    if move_number % 2 == 0:
        print("=========== Player 1 turn =============") 
        print_table(A)
        x = input("choose a number: ")

        try:
            x = int(x)
        except:
            print()
            print("======= you shoud choose number , Your turn was lost for this carelessness =======")
            print()
            continue       
        if 1<=x<=9 :
            put_number(x-1,"X")
            if Chek_win("X"):
                print_table(A)
                print("=========== Player 1 is won! =============")
                break           
        else:
            print()
            print("======= you shoud choose number between 1-9 , Your turn was lost for this carelessness =======")
            print()
            continue          
    else:
        print("=========== Player 2 turn =============") 
        print_table(A)
        x = input("choose a number: ")
        try:
            x = int(x)
        except:
            print()
            print("======= you shoud choose number , Your turn was lost for this carelessness =======")
            print()
            continue       
        if 1<=x<=9 :
            put_number(x-1,"O")
            if Chek_win("O"):
                print_table(A)
                print("=========== Player 1 is won! =============")
                break           
        else:
            print()
            print("======= you shoud choose number between 1-9 , Your turn was lost for this carelessness =======")
            print()
            continue     
print("table is full")