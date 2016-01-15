#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getPos()


mc.player.setPos(x,y+500,z)

