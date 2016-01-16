#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

x,y,z = mc.player.getPos()

mc.setBlocks(x,y+40,z,x+6,y+40+4,z+6,block.FENCE)
mc.setBlocks(x+1,y+41,z+1,x+1+4,y+41+2,z+1+4,block.AIR)
mc.player.setTilePos(x+3,y+42,z+3)
