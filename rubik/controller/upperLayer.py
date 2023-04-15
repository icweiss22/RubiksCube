from rubik.model.constants import * # @UnusedWildImport
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube):
    '''
        This is the top-level function for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''  
    solveUpperCorners(theCube)
    while not (1 == len(set(theCube.get()[0:9])) == len(set(theCube.get()[9:18])) == len(set(theCube.get()[18:27])) == len(set(theCube.get()[27:36])) == len(set(theCube.get()[36:45])) == len(set(theCube.get()[45:54]))):
        sideFaces = [theCube.get()[0:9], theCube.get()[9:18], theCube.get()[18:27], theCube.get()[27:36]]
        completeSide = next((i for i in sideFaces if len(set(i)) == 1), None)
        newOffset = 0
        if completeSide is not None:
            completeSideOffset = int(theCube.get().find(completeSide[0])/9)
            newOffset = (completeSideOffset + 2) % 4
        theCube.rotateWithOffset(newOffset, 'FFUrLFFlRUFF')

def solveUpperCorners(theCube: Cube):
    
    cornerArrays = [[0,2,4],[9,11,13],[18,20,22],[27,29,31]]
    middleBlocksArray = [4,13,22,31,40,49]

    while not(all(theCube.get()[i] == theCube.get()[j] == theCube.get()[k] for i,j,k in cornerArrays)): # corners have yet to be solved
        twoSameCorners = next((i for i in cornerArrays if theCube.get()[i[0]] == theCube.get()[i[1]]), None)
        newOffset = 0
        if twoSameCorners is not None:
            matchingMiddleCube = next((i for i in middleBlocksArray if theCube.get()[i] == theCube.get()[twoSameCorners[0]])) # the corresponding middle cube
            numberOfNeededRotations = int(matchingMiddleCube/9) - int(twoSameCorners[0]/9)
            if abs(numberOfNeededRotations) > 0:
                if numberOfNeededRotations > 0:
                    theCube.rotate(abs(numberOfNeededRotations)*'u')
                else:
                    theCube.rotate(abs(numberOfNeededRotations)*'U')
            middleCubeOffset = int(matchingMiddleCube/9) # 0 for front, 1 for right, 2 for back, 3 for left. now just need to align on left
            newOffset = (middleCubeOffset + 1) % 4
        theCube.rotateWithOffset(newOffset, 'lURuLUrRUrURUUr')