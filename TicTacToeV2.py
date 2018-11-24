# Tic Tac Toe        11.24.18                                            =
# © Woody Allen Montilus 2018                                            =
#                                                                        =
# This is an exercise that allowed me to get more comfortable with       =
# Python and applications for it. Version 2 allows for 1-2 player use    =
# ========================================================================

import random

# FUNCTIONS ==============================================================

# FORMATTING FUNCTIONS ===================================================

def sp(times): # print empty space for any given # of lines
    if times < 2:
        print()
    else:
        for i in range(times):
            print()

def stars(times): # Draws stars for any given # of lines
    if times < 2:
        print("***************************************************")
    else:
        for i in range(times):
            print("***************************************************")

def item_in_space(arr, index): # returns 'x', 'o', or ' ' for any given space
    try:
        arr[index]/1
        return " "
    except TypeError:
        return arr[index]
    
def board(arr): # Draws board with x's o's and spaces
    print("  " + item_in_space(arr, 0) + "  ||  " +
                 item_in_space(arr, 1) + "  ||  " +
                 item_in_space(arr, 2) + "  ")

    print("===================")

    print("  " + item_in_space(arr, 3) + "  ||  " +
                 item_in_space(arr, 4) + "  ||  " +
                 item_in_space(arr, 5) + "  ")

    print("===================")

    print("  " + item_in_space(arr, 6) + "  ||  " +
                 item_in_space(arr, 7) + "  ||  " +
                 item_in_space(arr, 8) + "  ")
def board_rules():
    print("This is the format that you'll be choosing from each turn:")
    sp(1)

    print("  " + str(0) + "  ||  " +
                 str(1) + "  ||  " +
                 str(2) + "  ")

    print("===================")

    print("  " + str(3) + "  ||  " +
                 str(4) + "  ||  " +
                 str(5) + "  ")

    print("===================")

    print("  " + str(6) + "  ||  " +
                 str(7) + "  ||  " +
                 str(8) + "  ")

    sp(1)
    stars(2)

    sp(4)

# ========================================================================
# DRIVING FUNCTIONS ======================================================

def new_board(): # Wipes board by reinitializing variable
    ticArr = [0, 1, 2, 3, 4, 5, 6, 7, 8] # Initializes "empty" board

def p_choice(arr, player): # Draws current board, and asks for a choice (positive int) for the next space to be taken; draws x or o based on who's turn it is
    board(arr)
    print("Player {}:".format(player))
    sp(1)
    turn = False
    while turn == False:
        good_choice = False
        while good_choice == False:

            good_num = False
            while good_num == False:
                p_input = input("What space will you take?    ")
                
                try:
                    p_input = float(p_input)
                    good_num = True
                except ValueError:
                    sp(1)
                    print("Please use integers")
                

            if p_input.is_integer() and p_input >= 0:
                good_choice = True
            else:
                sp(1)
                print("Please use positive integers")
                      
        sp(1)
        
        try:
            if player == 1:
                arr[arr.index(p_input)] = "x"
            else:
                arr[arr.index(p_input)] = "o"
            turn = True
        except ValueError:
            print("Oops! That space has already been taken!")
            turn = False
    
    sp(4)
    win_decide(arr)
    
def ez_ai_choice(arr, player):
    turn = False
    while turn == False:
        ai_input = random.randint(0, 9)
        
        try:
            if player == 1:
                arr[arr.index(ai_input)] = "x"
            else:
                arr[arr.index(ai_input)] = "o"
            turn = True
        except ValueError:
            turn = False
    print("Computer chose... Space {}".format(ai_input))
    sp(4)
    win_decide(arr)

def player(x_o): # Returns player number based on 'x' or 'o' use
    if x_o == "x":
        return 1
    elif x_o == "o":
        return 2
    else:
        return "N/A"

def win_decide(arr): # Runs through all possible winning formations and declares winner if any are true;
        if arr[0] == arr[1] and arr[0] == arr[2]:
            board(arr)
            sp(1)
            print("Player {} wins!".format(player(arr[0])))
            ask_quit()
            return True
        elif arr[3] == arr[4] and arr[3] == arr[5]:
            board(arr)
            sp(1)
            print("Player {} wins!".format(player(arr[3])))
            ask_quit()
            return True
        elif arr[6] == arr[7] and arr[6] == arr[8]:
            board(arr)
            sp(1)
            print("Player {} wins!".format(player(arr[6])))
            ask_quit()
            return True
        elif arr[0] == arr[3] and arr[0] == arr[6]:
            board(arr)
            sp(1)
            print("Player {} wins!".format(player(arr[0])))
            ask_quit()
            return True
        elif arr[1] == arr[4] and arr[1] == arr[7]:
            board(arr)
            sp(1)
            print("Player {} wins!".format(player(arr[1])))
            ask_quit()
            return True
        elif arr[2] == arr[5] and arr[2] == arr[8]:
            board(arr)
            sp(1)
            print("Player {} wins!".format(player(arr[2])))
            ask_quit()
            return True
        elif arr[0] == arr[4] and arr[0] == arr[8]:
            board(arr)
            sp(1)
            print("Player {} wins!".format(player(arr[0])))
            ask_quit()
            return True
        elif arr[2] == arr[4] and arr[2] == arr[6]:
            board(arr)
            sp(1)
            print("Player {} wins!".format(player(arr[2])))
            ask_quit()
            return True
        

def ask_quit(): # Asks if user would like to play again, and quits if not
    ask = input("Would you like to play again? 'y' or 'n'   ")
    sp(1)

    if ask != 'y':
        print("Thank you for playing!")
        raise SystemExit
    elif ask == 'y':
        print("Restarting...")
        new_board()
        
# =========================================================================

# =========================================================================



# DRIVING CODE ============================================================

print("Hello! Would you like to play against another person or against the computer?")
while True:
    
    good_game == False
    match_type = int(input("For PvP, press [1]; for PvC, press [2]"))


    if match_type == 1:
        stars(2)
        sp(1)
        print("INSTRUCTIONS:")
        sp(1)
        print("Please decide on your first and second players! ")
        
        board_rules()

        p_choice(ticArr, 1)
        p_choice(ticArr, 2)
        p_choice(ticArr, 1)
        p_choice(ticArr, 2)
        p_choice(ticArr, 1)
        p_choice(ticArr, 2)
        p_choice(ticArr, 1)
        p_choice(ticArr, 2)
        p_choice(ticArr, 1)

        print("The game is a tie!")
        ask_quit()

    elif match_type == 2:
        first_or_second = int(input("Would you like to go first or second? [1] or [2]"))

        stars(2)
        sp(1)
        print("INSTRUCTIONS:")
        board_rules()

        ticArr = [0, 1, 2, 3, 4, 5, 6, 7, 8] #Initializes "empty" board

        if first_or_second == 1:
            p_choice(ticArr, 1)
            ez_ai_choice(ticArr, 2)
            p_choice(ticArr, 1)
            ez_ai_choice(ticArr, 2)
            p_choice(ticArr, 1)
            ez_ai_choice(ticArr, 2)
            p_choice(ticArr, 1)
            ez_ai_choice(ticArr, 2)
            p_choice(ticArr, 1)

        elif first_or_second == 2:
            ez_ai_choice(ticArr, 1)
            p_choice(ticArr, 2)
            ez_ai_choice(ticArr, 1)
            p_choice(ticArr, 2)
            ez_ai_choice(ticArr, 1)
            p_choice(ticArr, 2)
            ez_ai_choice(ticArr, 1)
            p_choice(ticArr, 2)
            ez_ai_choice(ticArr, 1)

        print("The game is a tie!")
        ask_quit()
    else:
        print("Please choose [1] or [2]")


