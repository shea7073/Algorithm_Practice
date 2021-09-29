game_on = True
is_one = True

def game_start():
    player1 = "wrong"
    while player1 != "X" and player1 != "O":
        player1 = input("Player 1 would you like to be X or O?")

        if player1 != "X" and player1 != "O":
            print("Wrong input")
        else:
            print("Player 1 will go first")

    return player1


def ready():
    cont = "wrong"
    while cont != "Yes" and cont != "No":
        cont = input("Are you ready to play? Yes or No")
        if cont != "Yes" and cont != "No":
            print("Wrong Input")

    return cont


def draw_screen(screen):
    print("     " + "|" + "     " + "|" + "     ")
    print("  " + screen[0][0] + "  " + "|" + "  " + screen[0][1] + "  " + "|" + "  " + screen[0][2] + "  ")
    print("     " + "|" + "     " + "|" + "     ")
    print("------------------")
    print("     " + "|" + "     " + "|" + "     ")
    print("  " + screen[1][0] + "  " + "|" + "  " + screen[1][1] + "  " + "|" + "  " + screen[1][2] + "  ")
    print("     " + "|" + "     " + "|" + "     ")
    print("------------------")
    print("     " + "|" + "     " + "|" + "     ")
    print("  " + screen[2][0] + "  " + "|" + "  " + screen[2][1] + "  " + "|" + "  " + screen[2][2] + "  ")
    print("     " + "|" + "     " + "|" + "     ")


while game_on:
    spots = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("Welcome to Tic Tac Toe")
    choice1 = "wrong"
    choice2 = "wrong"
    winner = False

    p1 = game_start()
    if p1 == "X":
        p2 = "O"
    else:
        p2 = "X"

    ready = ready()

    if ready:
        draw_screen(spots)

    while not winner:
        while not choice1.isdigit() and choice1 not in range(0, 3):
            choice1 = input("Choose row (0,1,2)")
            choice_row = int(choice1)

        while not choice2.isdigit() and choice2 not in range(0, 3):
            choice2 = input("Choose col (0,1,2)")
            choice_col = int(choice2)

        if is_one:
            spots[choice_row][choice_col] = p1
        else:
            spots[choice_row][choice_col] = p2

        draw_screen(spots)

        is_one = not is_one

        choice1 = "wrong"
        choice2 = "wrong"

        for i in range(0, 3):
            if spots[i][0] == "X" and spots[i][1] == "X" and spots[i][2] == "X":
                print("X is the winner")
                winner = True
            if spots[i][0] == "O" and spots[i][1] == "O" and spots[i][2] == "O":
                print("O is the winner")
                winner = True
            if spots[0][i] == "X" and spots[1][i] == "X" and spots[2][i] == "X":
                print("X is the winner")
                winner = True
            if spots[0][i] == "O" and spots[1][i] == "O" and spots[2][i] == "O":
                print("O is the winner")
                winner = True

        if spots[1][1] == "X" and spots[0][0] == "X" and spots[2][2] == "X":
            print("X is the winner")
            winner = True

        if spots[1][1] == "O" and spots[0][0] == "O" and spots[2][2] == "O":
            print("X is the winner")
            winner = True

        if spots[1][1] == "X" and spots[0][2] == "X" and spots[2][0] == "X":
            print("X is the winner")
            winner = True

        if spots[1][1] == "O" and spots[0][2] == "O" and spots[2][0] == "O":
            print("O is the winner")
            winner = True

    replay = input("Would you like to play again? (y or n)")
    if replay == "y":
        pass
    else:
        game_on = False
