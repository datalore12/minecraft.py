#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

x,y,z=mc.player.getPos()

mc.setBlocks(x+2,y + -1, z,x+2+9,y+ -1 + 4, z+7,block.WOOD) 
mc.setBlocks(x+2,y+1,z,x+2+4,y+1+2,z+6,block.GLASS)
mc.setBlocks(x+3,y,z+1,x+3+7,y+0+2,z+1+5,block.AIR)
