from keyboard_alike import reader
from time import sleep
from shapes import *

reader = reader.Reader(0xffff, 0x0035, 84, 16, should_reset=False)

shapes = { "09144068" : cube,
           "18553444" : pyramid,
           "09359668" : diamond,
           "18720820" : prism,
           "09126404" : random_cube
           }

while True:
    reader.initialize()

    print("Ready")

    # shape is reset to an empty string so the while loop
    # can be used to error check bad input.
    shape = ""
    while shape not in shapes:
        shape = reader.read().strip()

    shapes[shape]()

    reader.disconnect()
    sleep(0.1)
