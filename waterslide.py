#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

x,y,z=mc.player.getPos()

xx = 0

for count in range(20):
	mc.setBlocks(x+xx,y+xx,z,x+xx+0,y+xx+0,z+0+1,block.STONE_BRICK)
	xx = xx + 1
mc.setBlocks(x+xx,y+xx+1,z,x+xx,y+xx+1+0,z+0+1,block.WATER_STATIONARY)
