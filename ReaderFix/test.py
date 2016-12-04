from keyboard_alike import reader


reader = reader.Reader(0xffff, 0x0035, 8, 8, should_reset=True)

reader.initialize()

while True:
     print(reader.read_card())


reader.disconnect()

    
