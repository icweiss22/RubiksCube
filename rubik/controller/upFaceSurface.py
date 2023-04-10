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
    if len(set(theCube.get()[36:45])) == 5: # need to set up for big turn
        while theCube.get()[LTR] != middleColor:
            theCube.rotate('u')
        theCube.rotate('RUrURUUr')        
    while len(set(theCube.get()[36:45])) != 1:
        fishFormation(theCube)
        
def fishFormation(theCube: Cube):
    while theCube.get()[UBL] != theCube.get()[UMM]:
        theCube.rotate('u')
    theCube.rotate('RUrURUUr')

        
