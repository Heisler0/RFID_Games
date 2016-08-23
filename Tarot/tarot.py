from random import Random
from time import sleep


random = Random()
fortunes = ["Yes", "No", "If you wish it, then so it shall be", "The answer is unclear",
             "Not in this lifetime", "There is potential", "Maybe, in the far future"]


#Main
main = True

try:
    print("Welcome to Python Tarot.")
    print("Where RNG will decide your destiny.")
    sleep(1)
    print("Use Ctrl + C at anytime to exit.\n")
    sleep(1)

    while main:
        try:
            card = raw_input("Scan your fortune card: ")
            random.seed(card)
            f = random.randrange(len(fortunes))
            print(".")
            sleep(1)
            print("..")
            sleep(1)
            print("...")
            sleep(1)
            print(fortunes[f] + "\n")
        except ValueError:
            print("Invalid input.\n")

except KeyboardInterrupt:
    print("Thanks for playing, bye bye.")
    
    
