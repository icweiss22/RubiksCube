from rubik.model.cube import Cube
from rubik.model.constants import *  # @UnusedWildImport
'''
Created on Feb 16, 2023

@author: isaacweiss
'''
def solveBottomCross(theCube: Cube):
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''  
    cubeStr = theCube.get()
    if not(cubeStr[DTM] == cubeStr[DML] == cubeStr[DMR] == cubeStr[DBM] == cubeStr[DMM]):
        makeCrossGeneric(theCube)
        
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


def makeCrossGeneric(theCube: Cube):        
    while any(theCube.get()[DMM] != theCube.get()[block] for block in [UTM,UML,UMR,UBM]):
        theCube.rotate('u')
        currentDMM = theCube.get()[DMM]
        
        # Front
        while theCube.get()[UBM] != currentDMM:
            F, R, u = 'F', 'R', 'u'
            if any(currentDMM == theCube.get()[i] for i in [12,32,46]):
                while theCube.get()[UBM] != currentDMM:
                    theCube.rotate(F)
            elif any(currentDMM == theCube.get()[i] for i in [1,3,5,7]):
                while currentDMM != theCube.get()[5]:
                    theCube.rotate(F)
                theCube.rotate(u + R)
            else:
                break
                
        # Right
        while theCube.get()[UMR] != currentDMM:
            F, R, u = 'R', 'B', 'u'
            if any(currentDMM == theCube.get()[i] for i in [5,21,50]):
                while theCube.get()[UMR] != currentDMM:
                    theCube.rotate(F)
            elif any(currentDMM == theCube.get()[i] for i in [10,12,14,16]):
                while currentDMM != theCube.get()[14]:
                    theCube.rotate(F)
                theCube.rotate(u + R)
            else:
                break
        
        # Back
        while theCube.get()[UTM] != currentDMM:
            F, R, u = 'B', 'L', 'u'
            if any(currentDMM == theCube.get()[i] for i in [14,30,52]):
                while theCube.get()[UTM] != currentDMM:
                    theCube.rotate(F)
            elif any(currentDMM == theCube.get()[i] for i in [19,21,23,25]):
                while currentDMM != theCube.get()[23]:
                    theCube.rotate(F)
                theCube.rotate(u + R)
            else:
                break
                
        # Left
        while theCube.get()[UML] != currentDMM:
            F, R, u = 'L', 'F', 'u'
            if any(currentDMM == theCube.get()[i] for i in [3,23,48]):
                while theCube.get()[UML] != currentDMM:
                    theCube.rotate(F)
            elif any(currentDMM == theCube.get()[i] for i in [28,30,32,34]):
                while currentDMM != theCube.get()[32]:
                    theCube.rotate(F)
                theCube.rotate(u + R)
            else:
                break