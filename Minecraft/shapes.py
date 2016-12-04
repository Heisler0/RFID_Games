import mcpi.minecraft as minc
import mcpi.block as blk
from random import Random

mc = minc.Minecraft.create()

# The block all the shapes will be made of.
# Go into each individual function to customize a shape's blocks
block = blk.MELON.id



def cube():

   length = 10
   
   x, y, z = mc.player.getPos()
   
   for i in range(length):
      for j in range(length):
         for k in range(length):
            mc.setBlock(x+i+1, y+j+1, z+k+1, c)



def pyramid():

   height = 10

   x, y, z = mc.player.getPos()

   level = height
   for i in range(height):
      length = (level * 2) - 1
      for j in range(length):
         for k in range(length):
            mc.setBlock(x+j+i, y+i, z+k+i, block)
      level -= 1



def diamond():

   height = 5

   x, y, z = mc.player.getPos()
    
   level = height
   for i in range(height):
       length = (level * 2) - 1
       for j in range(length):
           for k in range(length):
               mc.setBlock(x+j+i, y+height+i, z+k+i, block)
               mc.setBlock(x+j+i, y+height-i, z+k+i, block)
       level -= 1


# Spawn a hollow prism around the player
def prism():

   radius = 10

   x, y, z = mc.player.getPos()
    
   level = radius
   for i in range(radius):
       for j in range((-1*radius), radius):
           for k in range((-1*radius), radius):
               if(abs(j)+abs(k) + i + 1 == radius):
                   mc.setBlock(x+j, y+i, z+k, block)
                   mc.setBlock(x+j, y-i, z+k, block)
       level -= 1


# Generate a cube made of random colored WOOL blocks
def random_cube():
   r = Random()

   length = 25
   
   x, y, z = mc.player.getPos()
   
   for i in range(length):
      for j in range(length):
         for k in range(length):
            color = r.randint(0, 15)
            mc.setBlock(x+i+1, y+j+1, z+k+1, blk.WOOL.id, color)
