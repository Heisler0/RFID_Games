from InputHandler import getInput
from Character_v2 import Character
from time import sleep, time

while True:
    code = getInput()
    ch1 = Character(code)
    print("Generating your character...")
    sleep(2)
    print(ch1.name + " has entered.")
    print(ch1.abilities)
    print("\nGet ready to scan another Character.\n")
    sleep(2)



