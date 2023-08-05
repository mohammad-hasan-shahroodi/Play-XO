## play XO whit python 📼
![download](https://github.com/mohammad-hasan-shahroodi/Play-XO/assets/140893151/f6635c83-9afe-476c-b16a-6515d2fdb628)


Hello! Welcome to Shahroodi's game!
it's version 2 of XO game
Rules: Player 1 and player 2, represented by X and O, take turns marking the spaces in a 3*3 grid. 
#
also in the game 
### If the opener enters letter or enters a number greater than 9 or less than 1, he loses his turn.

![image](https://github.com/mohammad-hasan-shahroodi/Play-XO/assets/140893151/91dd9e92-2e38-4506-9b67-dff4d4cc5f90)

# XO - modern code :
in this code you make table with tow functions and also I use for a different list:
###
tow functions : 
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
- Sort the list :
```python
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
