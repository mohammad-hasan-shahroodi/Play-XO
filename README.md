## play XO whit python 📼
![download](https://github.com/mohammad-hasan-shahroodi/Play-XO/assets/140893151/f6635c83-9afe-476c-b16a-6515d2fdb628)


Hello! Welcome to Shahroodi's game!
it's version 2 of XO game
Rules: Player 1 and player 2, represented by X and O, take turns marking the spaces in a 3*3 grid. 
#
also in the game 
#### If the opener enters letter or enters a number greater than 9 or less than 1 or repeated number , The program finds out and asks them for a number again .

 ![image](https://github.com/mohammad-hasan-shahroodi/Play-XO/assets/140893151/91dd9e92-2e38-4506-9b67-dff4d4cc5f90)

# XO - modern code :
in this code you make table with tow functions and also I use for a different list:
###
- tow functions for sorting : 
```python
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
```
- list :
```python
A = [[0]*3 for i in range(3)]
```
- Error for  : If the opener enters letter or enters a number greater than 9 or less than 1 or repeated number , The program finds out :
```python
def error1():
    print("you should choose a number between 1-9, try agian:")
def error2():
    print("⓿_⓿")
    print("Don't cheat in the game , try agian: ")
    print("⓿_⓿")
```
```python
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
```
- checking for winner :
```python
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
```
```python
if Chek_win("X"):
    print_table(A)
    print("=========== Player 1 is won! =============")
    exit()
```
