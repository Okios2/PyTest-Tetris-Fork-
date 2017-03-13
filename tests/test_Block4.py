import pygame,sys,os
import sys
curdir=sys.path[0]
sys.path.insert(0,sys.path[0]+'/../mypkg')
import pytest
from Block4 import *
from Gameplay import *
b=0
a=300
bs=20
block=block4(a,b,bs)
game=Gameplay()
class Test_Block(object):
    def test_Blockinit(self):
        assert block.x1==a
        assert block.x2==a+bs
        assert block.x3==a
        assert block.x4==a-bs
        assert block.leftx==a-bs
        assert block.y1==b+bs
        assert block.y2==b+bs
        assert block.y3==b
        assert block.y4==b+bs
        assert block.lefty==b
        assert block.array==[[0,1,0],[1,1,1]]
        assert block.color==(0,0,0)
    def test_rotate(self):
        block=block4(300,60,20)
        block.rotate(game)
        assert block.x1==280
        assert block.x2==300
        assert block.x3==300
        assert block.x4==320
        assert block.y1==80
        assert block.y2==60
        assert block.y3==80
        assert block.y4==80
