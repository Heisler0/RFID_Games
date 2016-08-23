from InputHandler import getInput
from Character import Character
from time import sleep, time

while True:
    code = getInput()
    ch1 = Character(code)
    print("Generating your character...")
    sleep(2)
    print(ch1.name + " has entered.\n")
    print(ch1.abilities)
    sleep(2)



