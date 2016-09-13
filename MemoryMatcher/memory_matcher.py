from random import Random
from time import sleep, clock

#Set up game variables
cards = ["Jack", "Queen", "King", "Joker", "Ace", "Club", "Spade", "Diamon", "Heart"]
min_diff = 3
max_diff = len(cards)
random = Random(clock())

diff = 0
diff_sel = True


#Begin Game
print("Welcome to Memory Matcher!")
print("Begin by choosing your difficulty.")
#The player is prompted to select their difficulty
while diff_sel:
    try:
        diff = int(raw_input("\nEnter a number from 3 to 9: "))
        if diff >= 3 and diff <= 9:
            diff_sel = False
        else:
            print("Sorry, but that is not a valid number.") 
    except ValueError:
        print("Sorry, but that is not a valid number.")    

print("\nDifficulty Level " + str(diff) + " has been selected.")
max_strikes = diff - 1
sleep(1)
print("You have " + str(max_strikes) + " strikes to match " + str(diff) + " cards.")
print("If you reach " + str(max_strikes) + " strikes, you lose.")
print("if you match all the cards until only 1 remains, you win!\n")
sleep(2)

#Scanning loop
scanned = []

print("Scan in your playing cards.")
i = 0
while i < diff:
    card = raw_input("Scan a unique card now: ")
    if(card not in scanned):
        scanned.append(card)
        i += 1
    else:
        print("That card was already scanned, please scan another card.")

print("Success! All cards have been scanned.")

#Matching loop
running = True
while running:
    print("Good Luck!\n")
    sleep(1)
    #Set up game cards
    gameCards = []
    for i in range(diff):
        gameCards.append(cards[i])
        
    #Shuffle and Copy the scanned cards into a new variable
    random.shuffle(scanned)
    scannedCards = scanned[:]

    strikes = 0
    while strikes < max_strikes and len(gameCards) > 1:
        match = random.randrange(len(gameCards))
        print("You must find The " +  gameCards[match] + ".")
        guess = scannedCards.index(raw_input("Scan your guess: "))
        sleep(2)
        if guess == match:
            print("Great guess! You found The " + gameCards[match])
            gameCards.remove(gameCards[match])
            scannedCards.remove(scannedCards[match])
            print("Only " + str(len(gameCards)) + " to go, and you have " + str(strikes) + " strike(s).\n")
        else:
            strikes += 1
            print("You scanned The " + gameCards[guess] + ".")
            print("Sorry, but that is 1 strike.")
            print("You have a total of " + str(strikes) + " strike(s).\n")
        sleep(1)

    print("")
    if strikes >= max_strikes:
        print("You Lose.")
        print("You matched " + str(diff - len(gameCards)) + " cards.")
    else:
        print("Congratulations, You Win!")
        print("You managed to match all the cards with just " + str(strikes) + " strikes.")
        
    sleep(2)
    print("If you would like to play again just type: play")
    play = raw_input("--> ")
    if play != "play":
        running = False
    
print("Thanks for playing!")
print("Bye Bye!")






    
