#Character Game version 2.5
#Author(s) Chris Heisler

from InputHandler import getInput
from Pymon import Pymon
from time import sleep, clock
from random import Random

arenaName = "The Battle Frontier"
random = Random(clock())
rounds = 3

#Start Game
print("Welcome to " + arenaName + "!")

#Gane Loop
#Character Select
char_sel = True
while char_sel:
    #Player 1
    #Scan Player 1's card and use the number to generate a character
    print("\nPlayer 1, choose your Character.")
    code = getInput()
    ch1 = Pymon(code)
    print("Preparing your character...")
    sleep(2)
    print(ch1.name + " has entered the arena.\n")
    sleep(2)

    #Player 2
    #Scan Player 2's card and use the number to generate a character
    print("Player 2, choose you Character.")
    code = getInput()
    ch2 = Pymon(code)
    print("Preparing your character...")
    sleep(2)
    print(ch2.name + " has entered the arena.\n")
    sleep(2)

    #Battle Loop
    battle = True
    while battle:
        #Begin Battle
        print("\nThe battle begins in...")
        sleep(1)
        for i in range(3, 0, -1):
            print(i)
            sleep(1)
        print("Begin!\n")


        ch1_score = 0
        ch2_score = 0

        roundCounter = 1

        while roundCounter <= rounds and ch1_score <= rounds/2 and ch2_score <= rounds/2:
            index = roundCounter - 1
            round = "Round " + str(roundCounter)
            print(round)
            sleep(2)
            total = ch1.abilities[index] + ch2.abilities[index]
            result = random.randrange(total)
            if(result < ch1.abilities[index]):
                ch1_score += 1
                print("Player 1: " + ch1.name + " wins " + round + "\n") 
            else:
                ch2_score += 1
                print("Player 2: " + ch2.name + " wins " + round + "\n")
            roundCounter += 1
            sleep(1)

        print("Winner!")
        if(ch1_score > ch2_score):
            print("Player 1: " + ch1.name + " wins the battle!")
        else:
            print("Player 2: " + ch2.name + " wins the battle!")


        print("\nIf you would like to play again type: play")
        print("If you would like to reselect characters type: sel")
        choice = raw_input("Or press enter to quit --> ")
        if choice != "play":
            battle = False
            if choice != "sel":
                char_sel = False
        # IF the player does not type 'play' then exit the battle loop
        # Control returns to character selection loop IF the player types 'sel'
        # ELSE the game exits

print("Thanks for playing, bye bye.")
