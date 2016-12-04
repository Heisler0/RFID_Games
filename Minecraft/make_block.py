from keyboard_alike import reader
import mcpi.minecraft as minc
import mcpi.block as block
from time import sleep

reader = reader.Reader(0xffff, 0x0035, 84, 16, should_reset=False)

mc = minc.Minecraft.create()

blocks = { "09756356" : block.MELON.id,
           "19110900" : block.CACTUS.id,
           "09126404" : block.CHEST.id
           }


while True:
    reader.initialize()

    print("Ready")

    # block is reset to an empty string so the while loop
    # can be used to error check bad input.
    blk = ""
    while blk not in blocks:
        blk = reader.read().strip()

    (x, y, z) = mc.player.getPos()
    
    mc.setBlock(x, y, z, blocks[blk], 1)

    reader.disconnect()
    sleep(0.1)
    
