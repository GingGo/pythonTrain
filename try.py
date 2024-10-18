counter = 0

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def user_choice():
    choice = input("enter a number (1~9):")
    while not choice .isdigit() or int(choice) > 9 or int(choice) < 1:
        print("Enter isn't valid")
        choice = input("enter a number (1~9):")
    return int(choice)


def getCurrentSymbol():
    global counter
    counter += 1
    if counter % 2 == 1:
        return 'X'
    else:
        return 'O'


def update_table(index):
    if index in range(1, 4):
        if row1[index - 1] == " ":
            row1[index - 1] = getCurrentSymbol()
            return True
        else:
            return False
    elif index in range(4, 7):
        if row2[index % 3 - 1] == " ":
            row2[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False
    else:
        if row3[index % 3 - 1] == " ":
            row3[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False


def checkWinning():
    player_1_wins = False
    player_2_wins = False
    if (row1[0] == row1[1] and row1[1] == row1[2] and (" " not in row1)):
        if (row1[0] == 'X'):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row2[0] == row2[1] and row2[1] == row2[2] and (" " not in row2)):
        if (row2[0] == 'X'):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row3[0] == row3[1] and row3[1] == row3[2] and (" " not in row3)):
        if (row3[0] == 'X'):
            player_2_wins = True
        else:
            player_1_wins = True

    elif (row1[0] == row2[0] and row2[0] == row3[0] and (row1[0] != " ") and (row2[0] != " ") and (row3[0] != " ")):
        if (row1[0] == 'X'):
            player_2_wins = True
        else:
            player_1_wins = True

    elif (row1[1] == row2[1] and row2[1] == row3[1] and (row1[1] != " ") and (row2[1] != " ") and (row3[1] != " ")):
        if (row1[1] == 'X'):
            player_2_wins = True
        else:
            player_1_wins = True

    elif (row1[2] == row2[2] and row2[2] == row3[2] and (row1[2] != " ") and (row2[2] != " ") and (row3[2] != " ")):
        if (row1[2] == 'X'):
            player_2_wins = True
        else:
            player_1_wins = True

    elif (row1[0] == row2[1] and row2[1] == row3[2] and (row1[0] != " ") and (row2[1] != " ") and (row3[2] != " ")):
        if (row1[0] == 'X'):
            player_2_wins = True
        else:
            player_1_wins = True

    elif (row1[2] == row2[1] and row2[1] == row3[0] and (row1[2] != " ") and (row2[1] != " ") and (row3[0] != " ")):
        if (row1[2] == 'X'):
            player_2_wins = True
        else:
            player_1_wins = True

    if player_1_wins:
        return "Player 1 Wins"
    elif player_2_wins:
        return "Player 2 Wins"
    else:
        return "No one wins"


def startGame():
    while True:
        display(row1, row2, row3)
        if (" " not in row1) and (" " not in row2) and (" " not in row3):
            print("No one win")
            return

        while True:
            choice = user_choice()
            if update_table(choice):
                break
            else:
                print("Wrong position")
        ret = checkWinning()
        if ret == "Player 1 Wins":
            display(row1, row2, row3)
            print("Player 1 Wins")
            return
        elif ret == "Player 2 Wins":
            display(row1, row2, row3)
            print("Player 2 Wins")
            return


startGame()
