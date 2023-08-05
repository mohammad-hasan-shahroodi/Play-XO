print("Hello! Welcome to Shahroodi's game!")
print("\n")
print("Rules: Player 1 and player 2, represented by X and O, take turns "
"marking the spaces in a 3*3 grid. The player who succeeds in placing ")
print("\n")
input("Press enter to continue.")
print("\n")
msh = [1,2,3,4,5,6,7,8,9]
is_continue=True
turn = "X"
print("Here is the playboard: ")
print("-----------------------")
print("+---+---+---+")
print("|",msh[0], "|",msh[1], "|",msh[2],"|")
print("+---+---+---+")
print("|",msh[3], "|",msh[4], "|",msh[5],"|")
print("+---+---+---+")
print("|",msh[6], "|",msh[7], "|",msh[8],"|")
print("+---+---+---+")  
input("Press enter to continue.")
print("\n")
while is_continue:
    print("===========",turn," turn =============")
    print("+---+---+---+")
    print("|",msh[0], "|",msh[1], "|",msh[2],"|")
    print("+---+---+---+")
    print("|",msh[3], "|",msh[4], "|",msh[5],"|")
    print("+---+---+---+")
    print("|",msh[6], "|",msh[7], "|",msh[8],"|")
    print("+---+---+---+")
    print("-----------------------")
    n = input("get index:")
    print("-----------------------")

    try:
        n = int(n)
    except:
        print("=======Nemishe...=======")
        continue

    if 1<=n<=9 and msh[n-1] != "X" and msh[n-1] != "O":
        msh[n-1] = turn

    else:
        print("=======Nemishe...=======")

    if msh[0] == msh[1] == msh[2] or msh[3] == msh[4] == msh[5] or msh[6] == msh[7] == msh[8] or \
    msh[0] == msh[3] == msh[6] or msh[1] == msh[4] == msh[7] or msh[2] == msh[5] == msh[8] or \
    msh[0] == msh[4] == msh[8] or msh[2] == msh[4] == msh[6] :

        print("+---+---+---+")
        print("|",msh[0], "|",msh[1], "|",msh[2],"|")
        print("+---+---+---+")
        print("|",msh[3], "|",msh[4], "|",msh[5],"|")
        print("+---+---+---+")
        print("|",msh[6], "|",msh[7], "|",msh[8],"|")
        print("+---+---+---+")
        print('============================',turn,"is won!!!! ==================")
        break
    else:
        is_finished = False
        for a in range(9):
            if msh[a] == str(a+1):
                is_finished = True
        if is_finished == True:
            break

    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
