#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

x,y,z=mc.player.getPos()

mc.setBlocks(x+1,y,z,x+1+5,y+4,z+10,block.STONE_BRICK)
mc.setBlocks(x+2,y,z,x+2+3,y+3,z+10,block.AIR)
