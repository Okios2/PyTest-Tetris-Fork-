import pygame,sys,os
import sys
curdir=sys.path[0]
sys.path.insert(0,sys.path[0]+'/../mypkg')
import pytest
from Gameplay import *
def test_gameplayinit():
            gplay=Gameplay()
            #self.array=[[0]*30]*32
            assert gplay.array[0][0]==0
            assert gplay.array[0][30]==0
            assert gplay.array[31][0]==0
            assert gplay.array[31][30]==0
            assert gplay.colorarray[0][0]==0        #corner cases
            assert gplay.colorarray[0][30]==0        #corner cases
            assert gplay.colorarray[31][0]==0        #corner cases
            assert gplay.colorarray[31][30]==0        #corner cases
            assert gplay.block_size==20
#            assert gplay.__score==int(0)
 #           assert gplay.__level==int(1)
def test_checkRowFull():
            gplay=Gameplay()
            i=2
            test=gplay.checkRowFull()
            assert test==False
            for j in range(1,29):
                gplay.array[i][j]="X"
            test=gplay.checkRowFull()
            assert test!=False
def  test_checkRowEmpty():
            gplay=Gameplay()
            test=gplay.checkRowEmpty()
            assert test==True
            j=2
            for i in range(1,31):
                gplay.array[i][j]="X"
            test=gplay.checkRowEmpty()
            assert test==False
def test_emptyvalue():
            gplay=Gameplay()
            gplay.array[0][0]=='X'
            assert gplay.array[0][0]!='0'
            gplay.emptyvalue(0,0)
            assert gplay.array[0][0]=='0'
def test_delarray():
            gplay=Gameplay()
            i=0
            for j in range(1,29):
                gplay.array[i][j]="X"
            gplay.delarray(0)
            test=True
            for j in range(1,29):
                if gplay.array[i][j]=="X" or gplay.colorarray[i][j]!=0:
                    test=False
            assert test==True
def test_addfilledrow():
            gplay=Gameplay()
            gplay.addfilledrow()
            i=30
            test=True
            for j in range(1,29):
                if gplay.array[i][j]!='Y' and gplay.colorarray[i][j]!=0:
                    test=False
            assert test==True

def test_levelincrease():
            gplay=Gameplay()
            u=gplay.getlevel()
            gplay.increaselevel()
            v=gplay.getlevel()
            test=True
            if v-u!=1:
                true=False
            assert test==True
