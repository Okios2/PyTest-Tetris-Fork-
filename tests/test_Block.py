import pygame,sys,os                                                        
import sys
curdir=sys.path[0]
sys.path.insert(0,sys.path[0]+'/../mypkg')
import pytest
from Block import *
from Gameplay import *
b=0
a=300
bs=20
block=Block(a,b,bs)
game=Gameplay()
class Test_Block(object):
    def test_Blockinit(self):
        assert block.x1==a
        assert block.x2==a+bs
        assert block.x3==a
        assert block.x4==a+bs
        assert block.leftx==a
        assert block.y1==b
        assert block.y2==b
        assert block.y3==b+bs
        assert block.y4==b+bs
        assert block.lefty==b
        assert block.array==[[1,1],[1,1]]
        red=(255,0,0)
        assert block.color==red
    def test_moveRight(self):
        block=Block(a,b,bs)
        t1=block.x1
        t2=block.x2
        t3=block.x3
        t4=block.x4
        t5=block.leftx
        block.moveRight(bs)
        assert block.x1==t1+bs
        assert block.x2==t2+bs
        assert block.x3==t3+bs
        assert block.leftx==t5+bs
        assert block.x4==t4+bs
    def test_movedown(self):
        block=Block(a,b,bs)
        t1=block.y1
        t2=block.y2
        t3=block.y3
        t4=block.y4
        t5=block.lefty
        m=block.movedown(bs,game)
        assert block.y1==bs
        assert block.y2==t2+bs
        assert block.y3==t3+bs
        assert block.lefty==t5+bs
        assert block.y4==t4+bs
        assert m==True
    def test_moveup(self):
        block=Block(a,b,bs)
        t1=block.y1
        t2=block.y2
        t3=block.y3
        t4=block.y4
        t5=block.lefty
        m=block.moveup(bs)
        assert block.y1==t1-bs
        assert block.y2==t2-bs
        assert block.y3==t3-bs
        assert block.y4==t4-bs
        assert block.lefty==t5-bs
    def test_rotate(self):
        block=Block(300,60,20)
        block.rotate(game)
        assert block.x1==300
        assert block.x2==300
        assert block.x3==320
        assert block.x4==320
        assert block.y1==60
        assert block.y2==80
        assert block.y3==60
        assert block.y4==80
