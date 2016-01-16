#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

x,y,z = mc.player.getPos()

while not False:
	mc.setBlocks(x,y,z,x,y,z,block.LAVA_STATIONARY)
	time.sleep(3)
