from rubik.model.constants import *  # @UnusedWildImport
from rubik.model.cube import Cube
from rubik.controller.bottomCross import solveBottomCross

def solveBottomLayer(theCube: Cube):
    '''
        This is the top-level function for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''    
    while not(_checkBottomLayerSolved(theCube)): # while the bottom layer is not solved
        bottomColor = theCube.get()[49]
        # first, look for any whites in the top row
        topRowArray = [0,2,9,11,18,20,27,29]
        bottomRowArray = [6,8,15,17,24,26,33,35]
        middleBlocksArray = [4,13,22,31,40,49]
        while any(bottomColor == theCube.get()[i] for i in topRowArray):
            matchingCube = next((i for i in topRowArray if bottomColor == theCube.get()[i]), None)
            neighborCube = returnCorrespondingTopRowBlock(matchingCube) # array 0 is the actual corresponding neighbor, 1 is the center of that face
            matchingMiddleCube = next((i for i in middleBlocksArray if theCube.get()[neighborCube] == theCube.get()[i]), None)
            numberOfNeededRotations = int(matchingMiddleCube/9) - int(neighborCube/9)
            if abs(numberOfNeededRotations) > 0:
                if numberOfNeededRotations > 0:
                    theCube.rotate(abs(numberOfNeededRotations)*'u')
                else:
                    theCube.rotate(abs(numberOfNeededRotations)*'U')
            middleCubeOffset = int(matchingMiddleCube/9) # 0 for front, 1 for right, 2 for back, 3 for left, 4 for up, 5 for down
            if neighborCube % 9 == 0: # cubes on left, left trigger
                rotateWithOffset(middleCubeOffset, 'luL', theCube)
            else:
                rotateWithOffset(middleCubeOffset, 'RUr', theCube)
                
        if len(set(theCube.get()[45:54])) > 1: # this means the bottom is not all white, and that means there are whites on the bottom rows
            matchingBlock = next((i for i in bottomRowArray if bottomColor == theCube.get()[i]), None)      
            if matchingBlock is None: # the white block is on the top, do a right trigger to get it down
                theCube.rotate('RUr')
            elif matchingBlock % 9 == 8:
                rotateWithOffset(int(matchingBlock/9), 'RUrluLluL', theCube)
            else:
                rotateWithOffset(int(matchingBlock/9), 'luLRUrRUr', theCube)
            
def returnCorrespondingTopRowBlock(whiteBlock):
    topRowDictionary = {
        0: 29,
        2: 9,
        9: 2,
        11: 18,
        18: 11,
        20: 27,
        27: 20,
        29: 0
    }
    return topRowDictionary.get(whiteBlock, None)

def rotateWithOffset(offset, direction, theCube: Cube): # accepts offsets 0-3
    faces = {0: ('F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd'),
             1: ('R', 'r', 'B', 'b', 'L', 'l', 'F', 'f', 'U', 'u', 'D', 'd'),
             2: ('B', 'b', 'L', 'l', 'F', 'f', 'R', 'r', 'U', 'u', 'D', 'd'),
             3: ('L', 'l', 'F', 'f', 'R', 'r', 'B', 'b', 'U', 'u', 'D', 'd')}

    face_map = {'F': 0, 'f': 1, 'R': 2, 'r': 3, 'B': 4, 'b': 5, 'L': 6, 'l': 7, 'U': 8, 'u': 9, 'D': 10, 'd': 11}
    
    for char in direction:
        face = face_map[char]
        theCube.rotate(faces[offset][face])
            
def _checkBottomLayerSolved(theCube: Cube) -> bool:
    cubeStr = theCube.get()
    allBottom = len(set(cubeStr[45:54])) == 1
    botFront = all(cubeStr[4] == cubeStr[i] for i in [6,7,8])
    botRight = all(cubeStr[13] == cubeStr[i] for i in [15,16,17])
    botLeft = all(cubeStr[22] == cubeStr[i] for i in [24,25,26])
    botBack = all(cubeStr[31] == cubeStr[i] for i in [33,34,35])
    return allBottom and botFront and botRight and botLeft and botBack

def moveFrontCornersToTop(theCube: Cube):
    upCorners = [theCube.get()[UTL], theCube.get()[UTR], theCube.get()[UBL], theCube.get()[UBR]]
    if any(block == theCube.get()[DMM] for block in upCorners):
        if theCube.get()[UBL] == theCube.get()[DMM]:
                theCube.rotate('luuL')
        if theCube.get()[UBR] == theCube.get()[DMM]:
                theCube.rotate('RUUr')
        if theCube.get()[UTL] == theCube.get()[DMM]:
                theCube.rotate('LUUl')
        if theCube.get()[UTR] == theCube.get()[DMM]:
                theCube.rotate('ruuR')
                
def moveTopCornersDown(theCube: Cube):
    topCorners = [theCube.get()[FTL], theCube.get()[FTR], theCube.get()[RTL], theCube.get()[RTR], theCube.get()[BTL], theCube.get()[BTR], theCube.get()[LTL], theCube.get()[LTR]]
    FrontOffset, RightOffset, BackOffset, LeftOffset = 0, 9, 18, 27

    if any(block == theCube.get()[DMM] for block in topCorners):
        # Front
        if theCube.get()[FTL] == theCube.get()[DMM] or theCube.get()[FTR] == theCube.get()[DMM]:
            offset = FrontOffset
            F, f, R, r, B, b, L, l, U, u = 'F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u'
        # Right
        elif theCube.get()[RTL] == theCube.get()[DMM] or theCube.get()[RTR] == theCube.get()[DMM]:
            offset = RightOffset
            F, f, R, r, B, b, L, l, U, u = 'R', 'r', 'B', 'b', 'L', 'l', 'F', 'f', 'U', 'u'
        # Back
        elif theCube.get()[BTL] == theCube.get()[DMM] or theCube.get()[BTR] == theCube.get()[DMM]:
            offset = BackOffset
            F, f, R, r, B, b, L, l, U, u = 'B', 'b', 'L', 'l', 'F', 'f', 'R', 'r', 'U', 'u'
        # Left
        elif theCube.get()[LTL] == theCube.get()[DMM] or theCube.get()[LTR] == theCube.get()[DMM]:
            offset = LeftOffset
            F, f, R, r, B, b, L, l, U, u = 'L', 'l', 'F', 'f', 'R', 'r', 'B', 'b', 'U', 'u'
                
        if theCube.get()[offset + 2] == theCube.get()[DMM]:
            if theCube.get()[(offset + 9) % 36] == theCube.get()[(offset + 13) % 36]:
                theCube.rotate(f + u + F)
            elif theCube.get()[(offset + 9) % 36] == theCube.get()[(offset + 22) % 36]:
                theCube.rotate(u + r + u + R)
            elif theCube.get()[(offset + 9) % 36] == theCube.get()[(offset + 31) % 36]:
                theCube.rotate(u + u + b + u + B)
            elif theCube.get()[(offset + 9) % 36] == theCube.get()[(offset + 4) % 36]:
                theCube.rotate(U + l + u + L)
                
        if theCube.get()[offset + 0] == theCube.get()[DMM]:
            if theCube.get()[(offset + 29) % 36] == theCube.get()[(offset + 31) % 36]:
                theCube.rotate(F + U + f)
            elif theCube.get()[(offset + 29) % 36] == theCube.get()[(offset + 4) % 36]:
                theCube.rotate(u + R + U + r)
            elif theCube.get()[(offset + 29) % 36] == theCube.get()[(offset + 13) % 36]:
                theCube.rotate(u + u + B + U + b)
            elif theCube.get()[(offset + 29) % 36] == theCube.get()[(offset + 22) % 36]:
                theCube.rotate(U + L + U + l)
                    
