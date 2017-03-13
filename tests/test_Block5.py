import pygame,sys,os
import sys
curdir=sys.path[0]
sys.path.insert(0,sys.path[0]+'/../mypkg')
import pytest
from Block5 import *
from Gameplay import *
b=0
a=300
bs=20
block=block5(a,b,bs)
game=Gameplay()
class Test_Block(object):
    def test_Blockinit(self):
        assert block.x1==a
        assert block.x2==a+bs
        assert block.x3==a+2*bs
        assert block.x4==a+2*bs
        assert block.leftx==a
        assert block.y1==b
        assert block.y2==b
        assert block.y3==b
        assert block.y4==b+bs
        assert block.lefty==b
        assert block.array==[[1,1,1],[0,0,1]]
        assert block.color==(0,0,255)
    def test_rotate(self):
        block=block5(300,60,20)
        block.rotate(game)
        assert block.x1==300
        assert block.x2==300
        assert block.x3==320
        assert block.x4==340
        assert block.y1==60
        assert block.y2==80
        assert block.y3==60
        assert block.y4==60
