#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

x,y,z = mc.player.getPos()

mc.setBlocks(x+2,y,z,x+2+9,y,z+9,block.FENCE)
mc.setBlocks(x+3,y,z+1,x+3+7,y,z+1+7,block.FLOWER_YELLOW)

mc.setBlocks(x+2,y,z,x+2+9,y,z+0+9,block.FENCE)
mc.setBlocks(x+3,y,z+1,x+3+7,y,z+1+7,block.FLOWER_YELLOW)
