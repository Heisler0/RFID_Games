import sys, pygame, inputbox
from pygame import *

pygame.init()

#Window Size
size = (448, 388)
#Window Color
white = (255, 255, 255)
#Title Bar
display.set_caption("Screen Lock")

#Screen
screen = display.set_mode(size)
screen.fill(white)

#main
main = True
while main:
    password = inputbox.ask(screen, "Scan your Key Card")
    if password == "exit":
        pygame.quit()
    display.toggle_fullscreen()
    locked = True

    while locked:
        entry = inputbox.ask(screen, "Locked")
        if entry == "exit":
            pygame.quit()
        if password == entry:
            locked = False
            display.toggle_fullscreen()





