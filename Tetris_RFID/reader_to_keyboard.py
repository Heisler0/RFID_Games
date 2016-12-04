from keyboard_alike import reader
import uinput
from time import sleep

reader = reader.Reader(0xffff, 0x0035, 16, 4, should_reset=False, debug=True)
reader.initialize()

device = uinput.Device([
        uinput.KEY_UP,
        uinput.KEY_LEFT,
        uinput.KEY_DOWN,
        uinput.KEY_RIGHT
        ])

key_press = {
             "09144068" : uinput.KEY_UP,
             "09756356" : uinput.KEY_LEFT,
             "19110900" : uinput.KEY_DOWN,
             "09359668" : uinput.KEY_RIGHT
            }

while True:

    key = ""
    while key not in key_press:
        key = reader.read().strip()
    
    device.emit_click(key_press[key])

    sleep(0.1)
    
