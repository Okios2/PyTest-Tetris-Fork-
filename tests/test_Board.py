import pygame,sys,os
import sys
curdir=sys.path[0]
sys.path.insert(0,sys.path[0]+'/../mypkg')
import pytest
from Board import *
from Gameplay import *
class Test_board(object):
    def test_checkpiece(self):
        h=Board()
        arrayv=[[0,0,0,0,'X'],
                 [0,0,0,'X','X'],
                 [0,0,0,0,'X']
                ]
        test=True
        test=h.checkPiece(h,0,2,arrayv)
        assert test==False
        test=h.checkPiece(h,0,4,arrayv)
        assert test==True
        arrayv=[[0,0,0,'X','X'],
                 [0,0,0,'X','X'],
                 [0,0,0,0,0]
                ]
        test=h.checkPiece(h,0,4,arrayv)
        assert test==True
    def test_fillpiecepos(self):
        game=Gameplay()
        game.array[1][2]='X'
        h=Board()
        h.fillpiecepos(game,1,2,(255,0,0))
        assert game.array[3][4]==0
        assert game.array[1][2]=='X'
