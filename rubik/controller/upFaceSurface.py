from rubik.model.constants import * # @UnusedWildImport
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube):
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface  
    '''  
    middleColor = theCube.get()[UMM]
    potentialOuterEdgeCorners = [2,11,20,29]
    upSurfaceCorners = [36,38,42,44]

    while len(set(theCube.get()[36:45])) > 1: # while the top surface is not yet solved
        
        if len([i for i in upSurfaceCorners if theCube.get()[i] == middleColor]) == 1: # if fish formation detected
            while theCube.get()[UBL] != middleColor:
                theCube.rotate('u')
        elif any(middleColor == theCube.get()[i] for i in potentialOuterEdgeCorners):
            while theCube.get()[LTR] != middleColor:
                theCube.rotate('u')
        else:
            while theCube.get()[UBL] != middleColor:
                theCube.rotate('u')
        theCube.rotate('RUrURUUr')

        
