from rubik.model.constants import * # @UnusedWildImport
from rubik.model.cube import Cube
from rubik.controller.bottomLayer import solveBottomLayer, checkBottomLayerSolved

F, f, R, r, B, b, L, l, U, u, D, d = 'F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd'
def solveMiddleLayer(theCube: Cube):
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    '''  
    while not(checkMiddleLayerSolved(theCube)):
        upMiddleColor = theCube.get()[UMM]
        topArrays = [[37,19],[39,28],[41,10],[43,1]]
        middleBlocksArray = [4,13,22,31,40,49]
        checkMiddleBlocksLeft = [3,12,21,30]
        checkMiddleBlocksRight = [5,14,23,32]
        
        while any(upMiddleColor != theCube.get()[i[0]] and upMiddleColor != theCube.get()[i[1]] for i in topArrays): # looking around the top, while there are still blocks that dont match the UMM (top and side)
            missingTopArray = next((i for i in topArrays if upMiddleColor != theCube.get()[i[0]] and upMiddleColor != theCube.get()[i[1]]), None) # returning first pair of blocks where the top and side do not match the upper middle middle color
            matchingMiddleColorForSide = next((i for i in middleBlocksArray if theCube.get()[missingTopArray[1]] == theCube.get()[i]), None) # return corresponding middle block
            topColor = theCube.get()[missingTopArray[0]]
            numberOfNeededRotations = int(matchingMiddleColorForSide/9) - int(missingTopArray[1]/9) # if positive, it means middle color match is on a later face
            if abs(numberOfNeededRotations) > 0:
                if numberOfNeededRotations > 0:
                    theCube.rotate(abs(numberOfNeededRotations)*'u')
                else:
                    theCube.rotate(abs(numberOfNeededRotations)*'U')
            middleCubeOffset = int(matchingMiddleColorForSide/9) # 0 for front, 1 for right, 2 for back, 3 for left, 4 for up, 5 for down
            matchingMiddleColorForTop = next((i for i in middleBlocksArray if topColor == theCube.get()[i]), None) # now find middle block that matches top neighbor
            numberOfNeededRotationsForTop = int(matchingMiddleColorForTop/9) - middleCubeOffset
            if numberOfNeededRotationsForTop == -3 or numberOfNeededRotationsForTop == 1: # the result needs to be right-focused
                theCube.rotateWithOffset(middleCubeOffset, 'URUr')
            else: #left-focused
                theCube.rotateWithOffset(middleCubeOffset, 'uluL')
            solveBottomLayer(theCube)
                
        if not(checkMiddleLayerSolved(theCube)): # middle layer is still messed up despite satisfying the top conditions
            badMiddleArrayLeft = next((i for i in checkMiddleBlocksLeft if theCube.get()[i] != theCube.get()[i+1]), None)
            badMiddleArrayRight = next((i for i in checkMiddleBlocksRight if theCube.get()[i] != theCube.get()[i-1]), None)
            if badMiddleArrayLeft != None: # the error is indeed on the left side, do a left trigger
                theCube.rotateWithOffset(int(badMiddleArrayLeft/9), 'luL')
                solveBottomLayer(theCube)
            elif badMiddleArrayRight != None: # the error is indeed on the left side, do a left trigger
                theCube.rotateWithOffset(int(badMiddleArrayRight/9), 'RUr')
                solveBottomLayer(theCube)
            else: # don't know what happened, but do a left trigger on the front and hopefully that shuffles things around to fix it
                #theCube.rotateWithOffset(0, 'luL') 
                print('hello')               
            
def checkMiddleLayerSolved(theCube: Cube) -> bool:
    cubeStr = theCube.get()
    midFront = len(set(cubeStr[3:6])) == 1
    midRight = len(set(cubeStr[12:15])) == 1
    midLeft = len(set(cubeStr[21:24])) == 1
    midBack = len(set(cubeStr[30:33])) == 1
    return midFront and midRight and midLeft and midBack
