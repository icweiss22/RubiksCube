from rubik.model.cube import Cube
from rubik.model.constants import *  # @UnusedWildImport
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
    cubeStr = theCube.get()
    if not(cubeStr[DTM] == cubeStr[DML] == cubeStr[DMR] == cubeStr[DBM]):
        theCube.makeCrossGeneric()
        
        while theCube.get()[FTM] != theCube.get()[FMM]:
            theCube.rotate('U')
        theCube.rotate('FF')
            
        while theCube.get()[RTM] != theCube.get()[RMM]:
            theCube.rotate('U')
        theCube.rotate('RR')
            
        while theCube.get()[BTM] != theCube.get()[BMM]:
            theCube.rotate('U')
        theCube.rotate('BB')     
        
        while theCube.get()[LTM] != theCube.get()[LMM]:
            theCube.rotate('U')
        theCube.rotate('LL')
    
    return theCube.getSolution()    


