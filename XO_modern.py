A = [[0]*3 for i in range(3)]
print("Hello! Welcome to Shahroodi's game!")
print("it's version 2 of XO game")
print("\n")
print("Rules: Player 1 and player 2, represented by X and O, take turns "
"marking the spaces in a 3*3 grid. The player who succeeds in placing ")
print("\n")
input("Press enter to continue.")
print("\n")
def error1():
    print("you should choose a number between 1-9, try agian:")
def error2():
    print("⓿_⓿")
    print("Don't cheat in the game , try agian: ")
    print("⓿_⓿")
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
    if A[row][column] == "X" or A[row][column] == "O":
        return False
#    A[row][column] = R
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
def check_int(x):
    try:
        x = int(x)
    except:
        return False
def check_1_9(x):
    try:
        x = int(x)
    except:

        return False
    if not 1<=x<=9 :
        return False    
init_table(A)
for move_number in range(9):
    if move_number % 2 == 0:
        print("=========== Player 1 turn =============") 
        print_table(A)
        x = input("choose a number: ")
        while check_int(x) == False:
            error1()
            x = input("choose a number: ")
            check_int(x) 
        x = int(x)
        while check_1_9(x) == False:
            error1()
            x = input("choose a number: ")
            check_1_9(x)
        x = int(x)
        while put_number(x-1,"X") == False:
            error2()
            x = input("choose a number: ")
            while check_1_9(x) == False:
                error1()
                x = input("choose a number: ")
                check_1_9(x)
            x = int(x)
            put_number(x-1,"X")
        row = (x-1) // 3
        column = (x-1) % 3
        A[row][column] = "X"
        put_number(x-1,"X")
        if Chek_win("X"):
            print_table(A)
            print("=========== Player 1 is won! =============")
            exit()                    
         
    else:
        print("=========== Player 2 turn =============") 
        print_table(A)
        x = input("choose a number: ")
        while check_int(x) == False:
            error1()
            x = input("choose a number: ")
            check_int(x) 
        x = int(x)
        while check_1_9(x) == False:
            error1()
            x = input("choose a number: ")
            check_1_9(x)
        x = int(x)
        while put_number(x-1,"O") == False:
            error2()
            x = input("choose a number: ")
            while check_1_9(x) == False:
                error1()
                x = input("choose a number: ")
                check_1_9(x)
            x = int(x)
            put_number(x-1,"O")
        row = (x-1) // 3
        column = (x-1) % 3
        A[row][column] = "O"
        put_number(x-1,"O")
        if Chek_win("O"):
            print_table(A)
            print("=========== Player 2 is won! =============")
            exit()  
print("table is full")