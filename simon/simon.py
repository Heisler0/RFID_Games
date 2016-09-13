import sys, pygame, inputbox
from pygame import *
from random import Random
from time import sleep

#Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
colors = [red, green, blue, yellow]

#Screen
size = (448, 388)
display.set_caption("Simon")
screen = display.set_mode(size)

#Game variables
random = Random()
def color(c):
    screen.fill(c)
    display.update()
def gameover():
    for i in range(len(colors)):
        color(white)
        sleep(0.5)
        color(colors[i])
        sleep(0.5)
    color(black)
    sleep(3)
#Player's color cards
cards = []

#Scan player's cards
index = 0
while index < 4:
    screen.fill(colors[index])
    display.update()
    card = inputbox.ask(screen, "Scan a unique card")
    if(card not in cards):
        index = index + 1
        cards.append(card)
#Game loop
main = True
round = 1
while main:
    #Simon Sequence
    seq = []
    play = True
    while play:
        color(white)
        sleep(2)
        seq.append(random.randrange(4))
        for i in range(len(seq)):
            color(colors[seq[i]])
            sleep(1)
            color(white)
            sleep(0.25)
        color(white)
        i = 0
        while i < len(seq):
            sel = inputbox.ask(screen, "Scan your card")
            if cards.index(sel) != seq[i]:
                gameover()
                play = False
                i = len(seq)
            i = i + 1
           
    
    
