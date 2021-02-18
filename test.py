# milestone project 1

# set variables
playfield = 'dummy'
correct_playerchoice = ['X','x','O','o']
correct_playerturn = [0,1,2,3,4,5,6,7,8]
wtp = True

char0 = "0"
char1 = "1"
char2 = "2"

char3 = "3"
char4 = "4"
char5 = "5"

char6 = "6"
char7 = "7"
char8 = "8"

### declare all functions ###
# function to choose the icon for player 1
def choose_player():
    choice = False
    while choice == False:
        player1_choice = input('Hi player 1, please choose X or O: ')
        if player1_choice in correct_playerchoice:
            choice = True
            print(f"Thankyou, your choice was '{player1_choice}'")
        else:
            print(f"Please supply an correct value, note the captials. Your choice was '{player1_choice}'")
            choice = False
    return player1_choice

# function to print the playfield
def show_playfield():
    print(f" {char0} | {char1} | {char2} ")
    print("---+---+---")
    print(f" {char3} | {char4} | {char5} ")
    print("---+---+---")
    print(f" {char6} | {char7} | {char8} ")

# function to make player1 choice
def player1_turn():
    choice = False
    while choice == False:
        player1_turn = input('Please make a choice for your turn: (0-8)')
        print(player1_turn, correct_playerturn)
        if player1_turn.isdigit():
            player1_turn = int(player1_turn)
            if player1_turn in correct_playerturn:
                choice = True
                elementtopop = correct_playerturn.index(player1_turn)
                correct_playerturn.pop(elementtopop)
            else:
                pass
    return int(player1_turn)


# function to make player2 choice
def player2_turn():
    pass

# function to change characters
def execute_turn(player,charpos):
    if charpos == 0:
        char0 = player
    elif charpos == 1:
        char1 = player
    elif charpos == 2:
        char2 = player
    elif charpos == 3:
        char3 = player
    elif charpos == 4:
        char4 = player
        return 'char' + '4'
    elif charpos == 5:
        char5 = player
    elif charpos == 6:
        char6 = player
    elif charpos == 7:
        char7 = player
    elif charpos == 8:
        char8 = player
    else:
        print("something wrong")
    
# function to check for tictactoe

# function do you want to keep playing?
def want_to_play():
    choice = False
    correct_playchoice = ['Y','y','N','n']
    while choice == False:    
        want_to_playchoice = input('Do you want to keep playing? Y/N: ')
        if want_to_playchoice in correct_playchoice:
            if want_to_playchoice == 'Y' or want_to_playchoice == 'y':
                choice = True
                wtp = True
                print("thanks we will keep playing")
            else:
                choice = True
                wtp = False
                print("thankyou for playing")
        else:
            pass
    return wtp
### END of functions ###

### starting program ###
player1_choiceicon = choose_player()
while wtp:
    show_playfield()
    player1_turnchoice = player1_turn()
    execute_turn(player1_choiceicon,player1_turnchoice) = player1_turnchoice
    show_playfield()
    wtp = want_to_play()