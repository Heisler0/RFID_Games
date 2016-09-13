from time import sleep
from random import Random

#Variable Declerations
#Rounds start at 1
round = 1
#Min and Max # of players
min = 2
max = 4
random = Random()

#Main Loop

running = True
while running:
    #Welcome message and tutorial
    print("\nWelcome to KA-BOOM!")
    print("This is a " + str(min) + "-" + str(max) + " multiplayer game.")
    print("During each round the players take turns selecting and scanning a card.")
    print("Each card has a chance to trigger the bomb, and when triggered KA-BOOM! that player is eliminated from the game.")
    print("The round is over when a player is eliminated or one card remains.\n")
    sleep(3)

    #Player Loop
    player_lp = True
    while player_lp:
        try:
            players = int(raw_input("Please enter the number of players here: "))
            if players < min or players > max:
                print("The number of players must be between " + str(min) + " and " + str(max) + ".\n")
            else:
                player_lp = False
        except ValueError:
            print("You did not enter a valid number.\n")
    #Number of players has been declared.
    #End Player Loop

    #Card Scanning Loop
    scanning = True
    print("Scan your " + str(players + 1) + " playing cards now.")
    while scanning:
        cards_main = []
        for i in range(players + 1):
            cards_main.append(raw_input(str(i + 1) + ": "))
        sleep(1)
        print("If any of these card numbers are duplicates type: redo")
        cont = raw_input("Or press enter to continue --> ")
        if cont != "redo":
            scanning = False
    #End of Scanning Loop

    #Game Loop
    cards = cards_main[:]
    game = True
    while game:
        print("\nRound " + str(round))
        player = 1
        sleep(1)
        random.shuffle(cards)
        trigger = cards[random.randrange(len(cards))]
        used = []
        #Play Loop
        playing = True
        while playing:
            #Card Selection loop
            selecting = True
            while selecting:
                sel = raw_input("\nPlayer " + str(player) + " select your card: ")
                if((sel in cards) and (sel not in used)):
                    used.append(sel)
                    selecting = False                
                else:
                    print("That was not a valid card, please choose another card.")

            #End Selection Loop
            print("Tick...")
            sleep(1)
            print("Tick..")
            sleep(1)
            print("Tick.")
            sleep(1)

            if sel == trigger:
                print("KA-BOOM!!!")
                sleep(1)
                print("\nPlayer " + str(player) + " is eliminated.")
                cards.remove(trigger)
                playing = False
                
                #End of Game Check
                if len(cards) <= min:
                    print("\nCongratulations to the last player standing, you win!")
                    print("You survived " + str(round) + " round(s).")
                    sleep(2)
                    print("To play again type: play")
                    print("To change the number you players type: main")
                    choice = raw_input("Or press enter to exit --> ")
                    if choice == "play":
                        cards = cards_main[:]
                        round = 1
                        print("New Game, please have the same " + str(len(cards)) + " cards ready.")
                        sleep(3)
                    else:
                        game = False
                        if choice != "main":
                            running = False
                else:
                    print("Please remove the card they have selected from the game.")
                    round += 1
                    sleep(3)

            else:
                print("Pffff...")
                sleep(1)
                print("Player " + str(player) + " survives this time.")
                player += 1

                if player >= len(cards):
                    print("All the players have survived, on to the next round.")
                    round += 1
                    playing = False
        #End Play Loop
    #End of Game Loop              
#End of Main Loop
print("\nThanks for playing, bye bye.")
        


    
