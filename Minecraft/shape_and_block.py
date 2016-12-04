import mcpi.minecraft as minc
import mcpi.block as block
from random import Random

mc = minc.Minecraft.create()

blocks = { "09756356" : block.MELON.id,
           "19110900" : block.CACTUS.id,
           "09126404" : block.CHEST.id
           }

def read(reader):
   reader.disconnect()
   reader.initialize()

   # block is reset to an empty string so the while loop
   # can be used to error check bad input.
   blk = ""
   while blk not in blocks:
       print("Scan Block")
       mc.postToChat("Scan Block")
       blk = reader.read().strip()

   blk = blocks[blk]

   #reader.disconnect()

   return blk
    


def cube(reader):
   blk = read(reader)
   
   length = 10
   
   x, y, z = mc.player.getPos()
   
   for i in range(length):
      for j in range(length):
         for k in range(length):
            mc.setBlock(x+i+1, y+j+1, z+k+1, blk)



def pyramid(reader):
   blk = read(reader)

   height = 10

   x, y, z = mc.player.getPos()

   level = height
   for i in range(height):
      length = (level * 2) - 1
      for j in range(length):
         for k in range(length):
            mc.setBlock(x+j+i, y+i, z+k+i, blk)
      level -= 1



def diamond(reader):
   blk = read(reader)

   height = 20

   x, y, z = mc.player.getPos()
    
   level = height
   for i in range(height):
       length = (level * 2) - 1
       for j in range(length):
           for k in range(length):
               mc.setBlock(x+j+i, y+height+i, z+k+i, blk)
               mc.setBlock(x+j+i, y+height-i, z+k+i, blk)
       level -= 1


# Spawn a hollow prism around the player
def prism(reader):
   blk = read(reader)

   radius = 10

   x, y, z = mc.player.getPos()
    
   level = radius
   for i in range(radius):
       for j in range((-1*radius), radius):
           for k in range((-1*radius), radius):
               if(abs(j)+abs(k) + i + 1 == radius):
                   mc.setBlock(x+j, y+i, z+k, blk)
                   mc.setBlock(x+j, y-i, z+k, blk)
       level -= 1


# Generate a cube made of random colored WOOL blocks
def random_cube():   
   r = Random()

   length = 10
   
   x, y, z = mc.player.getPos()
   
   for i in range(length):
      for j in range(length):
         for k in range(length):
            color = r.randint(0, 15)
            mc.setBlock(x+i+1, y+j+1, z+k+1, blk.WOOL.id, color)
