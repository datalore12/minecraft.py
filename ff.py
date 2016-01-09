#This is the ForceField script

#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getPos()

air = 0

while True:
	mc.setBlock(x-3,y,z-3,6,4,6, air)

