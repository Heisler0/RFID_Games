import sys
import pygame, inputbox
from pygame import *
from pygame.mixer import Sound
from time import sleep

pygame.init()
pygame.mixer.init()

# Window Size
SIZE = (448, 388)

# Window Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Display the window
window = display.set_mode(SIZE)
display.set_caption("Cardlock")

# Set up sound variables
lock = Sound("lock.wav")
unlock = Sound("unlock.wav")
airhorn = Sound("airhorn.wav")

# Master key
KEY = "exit"

while True:
    window.fill(GREEN)
    keycard = inputbox.ask(window, "Scan your keycard to lock") # My Keycard ID Number
    if keycard == KEY:
        pygame.quit()
    display.toggle_fullscreen()
    lock.play()
    locked = True

    while locked:
        window.fill(RED)
        entry = inputbox.ask(window, "Locked")
        if entry == keycard:
            locked = False
            unlock.play()
            display.toggle_fullscreen()
        elif entry == KEY:
            pygame.quit()
        else:
            airhorn.play()
    sleep(0.2)
