#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getPos()

mc.setBlocks(x+1,y+0,z+1, x+2, y+10, z+2, block.TNT, 1)
mc.setBlocks(x+1,y+11,z+1,x+2,y+12,z+2,block.LAVA_STATIONARY)
