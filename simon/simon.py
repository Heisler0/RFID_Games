import sys, pygame
from keyboard_alike import reader
from pygame import *
from pygame.mixer import Sound
from random import Random
from time import sleep
 
pygame.font.init()
 
#Game variables
 
random = Random()
 
round = 1
 
reader = reader.Reader(0xffff, 0x0035, 8, 8, should_reset=False)
 
#Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
colors = [red, green, blue, yellow]
 
#RFID dictionary, maps cards to colors
cards = {
            "09756356" : red,
            "09359668" : green,
            "09144068" : blue,
            "19110900" : yellow
            }
 
#Screen
size = (448, 388)
display.set_caption("Simon")
screen = display.set_mode(size)
 
#Change the screen color
##def color(c):
##    screen.fill(c)
##    display.update()
 
#On incorrect guess, screen flashes all colors
def gameover():
    for i in range(len(colors)):
        setDisplay(white, "Game Over")
        sleep(0.35)
        setDisplay(colors[i], "Game Over")
        sleep(0.35)
    setDisplay(black)
    sleep(1)
    pygame.quit()
 
#Text Display
default = font.get_default_font()
font = font.Font(default, 60)
x = 50
y = 100
 
#Change the screen color, and if text is provided set text to the screen
def setDisplay(c, s=""):
    screen.fill(c)
    text = font.render(s, True, black)
    screen.blit(text, (x, y))
    display.update()
 
#Color names
strings = {
            red : "RED",
            green : "GREEN",
            blue : "BLUE",
            yellow : "YELLOW"
            }
 
 
#Simon Sequence
seq = []
 
#Game loop
play = True
while play:
    reader.initialize()
    setDisplay(white, "Round " + str(round))
    sleep(1.5)
    setDisplay(white, "Simon Says")
    sleep(2)
    seq.append(random.choice(colors))
 
       
    for i in range(len(seq)):
        c = seq[i]
        setDisplay(c, strings[c])
        sleep(1)
        setDisplay(white)
        sleep(0.25)
    setDisplay(white)
 
    j = 0
    while j < len(seq) and play:
 
        sel = ""
        while sel not in cards:
            sel = reader.read_card()  
       
        c = cards[sel]
        setDisplay(white, strings[c])
 
        if c != seq[j]:
            sleep(1)
            gameover()
            play = False
 
        j += 1
 
    round += 1
 
    reader.disconnect()
    sleep(1)
