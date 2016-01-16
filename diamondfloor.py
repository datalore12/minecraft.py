#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

x, y, z = mc.player.getPos()

mc.setBlocks(x-1,y-1,z-1,x-1+10,y-1,z-1+10,block.DIAMOND_BLOCK)
