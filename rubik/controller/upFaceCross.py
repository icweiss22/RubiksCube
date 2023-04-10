from rubik.model.constants import *  # @UnusedWildImport
from rubik.model.cube import Cube

def solveUpCross(theCube: Cube):
    '''
        This is the top-level function  for rotating
        a cube into the up-face cross configuration.
        
        input:  an instance of the cube class with the middle layer solved
        output: the rotations required to solve the up-face cross  
    '''  
    while not(theCube.get()[UMM] == theCube.get()[UML] == theCube.get()[UMR] == theCube.get()[UTM] == theCube.get()[UBM]):
        
        if theCube.get()[UTM] == theCube.get()[UMR]:
            theCube.rotate('u')
        elif theCube.get()[UBM] == theCube.get()[UML]:
            theCube.rotate('U')
        elif theCube.get()[UBM] == theCube.get()[UMR]:
            theCube.rotate('uu')
        
        theCube.rotate('FURurf')