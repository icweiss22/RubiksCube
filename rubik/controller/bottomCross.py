from rubik.model.cube import Cube
from rubik.model.constants import *  # @UnusedWildImport

TwoFront, TwoRight, TwoBack, TwoLeft = 'FF', 'RR', 'BB', 'LL'
U = 'U'
'''
Created on Feb 16, 2023

@author: isaacweiss
'''
def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''  
    bottomCross = [theCube.get()[DTM], theCube.get()[DML], theCube.get()[DMR], theCube.get()[DBM]]
    if any(tileInBottomCross != theCube.get()[DMM] for tileInBottomCross in bottomCross):
        theCube.makeCrossGeneric()
        if theCube.get()[FTM] != theCube.get()[FMM]: # Front 
            while True:
                theCube.rotate(U)
                if theCube.get()[FTM] == theCube.get()[FMM]:
                    break
            theCube.rotate(TwoFront)
        else:
            theCube.rotate(TwoFront)
            
        if theCube.get()[RTM] != theCube.get()[RMM]: # Right
            while True:
                theCube.rotate(U)
                if theCube.get()[RTM] == theCube.get()[RMM]:
                    break
            theCube.rotate(TwoRight)
        else:
            theCube.rotate(TwoRight)
            
        if theCube.get()[BTM] != theCube.get()[BMM]: # Back
            while True:
                theCube.rotate(U)
                if theCube.get()[BTM] == theCube.get()[BMM]:
                    break
            theCube.rotate(TwoBack)
        else:
            theCube.rotate(TwoBack)
            
        
        if theCube.get()[LTM] != theCube.get()[LMM]: # Left
            while True:
                theCube.rotate(U)
                if theCube.get()[LTM] == theCube.get()[LMM]:
                    break
            theCube.rotate(TwoLeft)
        else:
            theCube.rotate(TwoLeft)
    
    return theCube.getSolution()    


