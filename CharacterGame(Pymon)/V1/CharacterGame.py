from InputHandler import getInput
from Character import Character
from time import sleep, clock
from random import Random

arenaName = "The Thunder Dome"
random = Random(clock())
rounds = 3

#Start Game
print("Welcome to " + arenaName + "!\n")

#Player 1
print("Player 1, choose your Character.")
code = getInput()
ch1 = Character(code)
print("Preparing your character...")
sleep(2)
print(ch1.name + " has entered.\n")
sleep(2)

#Player 2
print("Player 2, choose you Character.")
code = getInput()
ch2 = Character(code)
print("Preparing your character...")
sleep(2)
print(ch2.name + " has entered.\n")
sleep(2)

#Begin Battle
print("The battle begins in...")
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

 
    


