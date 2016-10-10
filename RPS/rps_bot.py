from time import sleep
from getpass import getpass
from random import Random

#Python Rock, Paper, Scissors using RFID reader
#Author(s): Christopher Heisler

#Set up variables
rounds = 3
win_c = (rounds/2) + 1
random = Random()

#Define our functions now to be used later in the game

# @return 0 corresponds to Rock, 1 to Paper, 2 tp scissors
def cardSelect(playerName, playerCards):
    while True:
        sel = getpass(playerName + ", select your card.")
        for i in range(len(playerCards)):
            if playerCards[i] == sel:
                return i
        print("I'm sorry, that card appears invalid. Please scan a valid card.")
        sleep(1)
        
# Process a round given both players' selections
# @return 0 if a draw, else 1 if player 1 wins, else 2
def processRound(player1_sel):
    print("\nRock")
    sleep(1)
    print("Paper")
    sleep(1)
    print("Scissors")
    sleep(1)
    print("Shoot!")

    choices = ["Rock.", "Paper.", "Scissors."]
    player2_sel = random.randint(0, 2)
    sleep(1)
    print("\nPlayer 1 has selected " + choices[player1_sel])
    sleep(1)
    print("Player 2 has selected " + choices[player2_sel] + "\n")
    if player1_sel == player2_sel:
        return 0
    if player1_sel == 0:
        if player2_sel == 2:
            return 1
        else:
            return 2
    if player1_sel == 1:
        if player2_sel == 0:
            return 1
        else:
            return 2
    if player1_sel == 2:
        if player2_sel == 1:
            return 1
        else:
            return 2


#End of function definitions



##############################################
#Begin the game
print("Welcome to Python Rock, Paper, Scissors.")
print("Have your 3 playing cards ready.")
sleep(1)
#First scan in the players' cards

#Scanning Player 1's cards
sleep(2)
print("Player 1, scan your playing cards.")
sleep(1)
scanning = True

while scanning:
    player1 = [raw_input("Scan your Rock card: "),
               raw_input("Scan your Paper card: "),
               raw_input("Scan your Scissor card: ")]
    if raw_input("\nIf any of these card IDs are duplicates please type \'redo\', or else press enter to continue: ") != "redo":
          scanning = False

sleep(1)
print("Success! Player 1\'s cards have been scanned.\n") 

#Game loop
running = True

while running:
    
    #Then start the rounds
    sleep(2)
    print("\nNow, let the match begin!")
    sleep(1)
    print("This match will be a best off " + str(rounds))
    sleep(1)
    print("Each player must win " + str(win_c) + " rounds to win the entire match!\n")
    sleep(2) 


    #Main functionality of the game begins here
    player1_wins = 0
    player2_wins = 0

    round = 1

    while round <= rounds and player1_wins < win_c and player2_wins < win_c:
        round_str = str(round)
        print("Round " + round_str + ":")

        player1_select = cardSelect("Player 1", player1)
        result = processRound(player1_select)

        if result == 1:
            print("Player 1 wins round " + round_str + ".")
            player1_wins += 1
            round += 1
        elif result == 2:
            print("Player 2 wins round " + round_str + ".")
            player2_wins += 1
            round += 1
        else:
            print("Round " + round_str + " resulted in a draw, the round will recommemce.\n")
        sleep(1)
        if result != 0:
            print("The score is: " + "Player 1: " + str(player1_wins) + "    Player 2: " + str(player2_wins))
            print("End of round " + round_str + ".\n")
        sleep(2)
        

    if player1_wins == player2_wins:
        print("The match has ended in a draw.")
    elif player1_wins > player2_wins:
        print("Player 1 has won the match!")
    else:
        print("Player 2 has won the match!")

    #Replay?
    sleep(1)
    print("\nIf you would like to play again press enter.")
    if raw_input("Or type quit to exit the game: ") == "quit":
        running = False
    #End of Game Loop

print("\nGame Over, thanks for playing.")
#End of Game
###################################


        
