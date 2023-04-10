from rubik.model.constants import *  # @UnusedWildImport
from rubik.model.cube import Cube
from rubik.controller.bottomCross import solveBottomCross

def solveBottomLayer(theCube: Cube):
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''    
    # Loop while bottom layer is not yet solved
    while any(block != theCube.get()[DMM] for block in [theCube.get()[DTL], theCube.get()[DTM], theCube.get()[DTR], theCube.get()[DML], theCube.get()[DMR], theCube.get()[DBL], theCube.get()[DBM], theCube.get()[DBR]]):
        '''
        Bottom corners -> Up
        '''
        cubeStr = theCube.get()
        FrontOffset, RightOffset, BackOffset, LeftOffset = 0, 9, 18, 27
        if any(block == cubeStr[DMM] for block in [cubeStr[FBL], cubeStr[FBR], cubeStr[RBL], cubeStr[RBR], cubeStr[BBL], cubeStr[BBR], cubeStr[LBL], cubeStr[LBR]]):
            # Front
            if cubeStr[FBL] == cubeStr[DMM] or cubeStr[FBR] == cubeStr[DMM]:
                offset = FrontOffset
                R, r, L, l, U, u = 'R', 'r', 'L', 'l', 'U', 'u'
            # Right
            elif cubeStr[RBL] == cubeStr[DMM] or cubeStr[RBR] == cubeStr[DMM]:
                offset = RightOffset
                R, r, L, l, U, u = 'B', 'b', 'F', 'f', 'U', 'u'
            # Back
            elif cubeStr[BBL] == cubeStr[DMM] or cubeStr[BBR] == cubeStr[DMM]:
                offset = BackOffset
                R, r, L, l, U, u = 'L', 'l', 'R', 'r', 'U', 'u'
            # Left
            elif cubeStr[LBL] == cubeStr[DMM] or cubeStr[LBR] == cubeStr[DMM]:
                offset = LeftOffset
                R, r, L, l, U, u = 'F', 'f', 'B', 'b', 'U', 'u'
            
            if theCube.get()[offset + 6] == theCube.get()[DMM]:
                theCube.rotate(l + u + L)
            if theCube.get()[offset + 8] == theCube.get()[DMM]:
                theCube.rotate(R + U + r)
            
        '''
        Front corners -> Top
        '''
        moveFrontCornersToTop(theCube)
            
        '''
        Top corners -> Down
        '''
        moveTopCornersDown(theCube)
            
        btmCross = [theCube.get()[DTM], theCube.get()[DMR], theCube.get()[DBM], theCube.get()[DML]]
        if not all(block == theCube.get()[DMM] for block in btmCross):
            solveBottomCross(theCube)

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
                    
