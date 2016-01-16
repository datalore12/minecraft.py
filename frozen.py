#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

x,y,z=mc.player.getPos()

while not False:
	time.sleep(0.2)
	if mc.getBlockWithData(x,y,z) == block.WATER_STATIONARY:
		mc.setBlocks(x,y,z,x,y,z,block.ICE)
