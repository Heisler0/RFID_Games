from random import Random
from time import sleep

random1 = Random()
random2 = Random()
highscore = 0
score = 0

#Game Intro
print("Welcome to No Wammies!")
sleep(1)
print("The objective of the game is to score as many points as possible before hitting a wammie.")
print("You play by scanning a card, that card will either reward you no points, 10 points, 50 points, or it will be a wammie and end the game.")
sleep(3)
print("Good luck!")
sleep(1)


def numberGenerator(seed):
    random1.seed(seed)
    r = []
    r.append(random1.randint(1, 6))
    for i in range (1, 6):
        r.append(random2.randint(1, 6))
    return random2.choice(r)

#Main
main = True

#Notes
# 0 = 0 points
# 1 or 2 = 10 points
# 3 = 50 points
# 4 or 5 = Wammie
while main:
    print("\nScore: " + str(score))
    card = raw_input("Select a card: ")
    number = numberGenerator(card)
    if number > 3:
        print("\nWammie! Game over.")
        print("Your final score is " + str(score) + ".")
        sleep(1)
        if score > highscore:
            highscore = score
            print("New highscore!")
        else:
            print("Current highscore is " + str(highscore) + ".")
        sleep(1)
        print("\nNew game starting now.")
    elif number == 0:
        print("Pffff...that's a dud, no points.")
    elif number == 3:
        print("Jackpot! 50 points.")
        score = score + 50
    else:
        print("10 points, nice!")
        score = score + 10
    sleep(1)
    
