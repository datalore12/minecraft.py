#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()
x,y,z=mc.player.getPos()

mc.setBlocks(x,y+15,z,x+15,y+30,z+15,block.WATER_STATIONARY)
