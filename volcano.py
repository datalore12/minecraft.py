#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

x,y,z=mc.player.getPos()

mc.setBlocks(x+1, y, z+1,x+1+1,y+10,z+1+1,block.STONE_BRICK)
mc.setBlocks(x+1,y+11,z+1,x+1+1, y+11+1,z+1+1,block.LAVA_STATIONARY)
