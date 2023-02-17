from rubik.model.constants import *  # @UnusedWildImport
from rubik.model.cube import Cube
from rubik.controller.bottomCross import solveBottomCross

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''    
    # Loop while bottom layer is not yet solved
    while any(i != theCube.get()[DMM] for i in [theCube.get()[DTL], theCube.get()[DTM], theCube.get()[DTR], theCube.get()[DML], theCube.get()[DMR], theCube.get()[DBL], theCube.get()[DBM], theCube.get()[DBR]]):
        '''
        Bottom corners -> Up
        '''
        btmCorners = [theCube.get()[FBL], theCube.get()[FBR], theCube.get()[RBL], theCube.get()[RBR], theCube.get()[BBL], theCube.get()[BBR], theCube.get()[LBL], theCube.get()[LBR]]
        if any(i == theCube.get()[DMM] for i in btmCorners):
            # Front
            if theCube.get()[FBL] == theCube.get()[DMM] or theCube.get()[FBR] == theCube.get()[DMM]:
                offset = 0
                F, f, R, r, B, b, L, l, U, u = 'F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u'
            # Right
            elif theCube.get()[RBL] == theCube.get()[DMM] or theCube.get()[RBR] == theCube.get()[DMM]:
                offset = 9
                F, f, R, r, B, b, L, l, U, u = 'R', 'r', 'B', 'b', 'L', 'l', 'F', 'f', 'U', 'u'
            # Back
            elif theCube.get()[BBL] == theCube.get()[DMM] or theCube.get()[BBR] == theCube.get()[DMM]:
                offset = 18
                F, f, R, r, B, b, L, l, U, u = 'B', 'b', 'L', 'l', 'F', 'f', 'R', 'r', 'U', 'u'
            # Left
            elif theCube.get()[LBL] == theCube.get()[DMM] or theCube.get()[LBR] == theCube.get()[DMM]:
                offset = 27
                F, f, R, r, B, b, L, l, U, u = 'L', 'l', 'F', 'f', 'R', 'r', 'B', 'b', 'U', 'u'
            
            if theCube.get()[offset + 6] == theCube.get()[DMM]:
                theCube.rotate(l + u + L)
            if theCube.get()[offset + 8] == theCube.get()[DMM]:
                theCube.rotate(R + U + r)
            
        '''
        Front corners -> Top
        '''
        upCorners = [theCube.get()[UTL], theCube.get()[UTR], theCube.get()[UBL], theCube.get()[UBR]]
        if any(i == theCube.get()[DMM] for i in upCorners):
            if theCube.get()[UBL] == theCube.get()[DMM]:
                theCube.rotate('luuL')
            if theCube.get()[UBR] == theCube.get()[DMM]:
                theCube.rotate('RUUr')
            if theCube.get()[UTL] == theCube.get()[DMM]:
                theCube.rotate('LUUl')
            if theCube.get()[UTR] == theCube.get()[DMM]:
                theCube.rotate('ruuR')
            
        '''
        Top corners -> Down
        '''
        topCorners = [theCube.get()[FTL], theCube.get()[FTR], theCube.get()[RTL], theCube.get()[RTR], theCube.get()[BTL], theCube.get()[BTR], theCube.get()[LTL], theCube.get()[LTR]]
        if any(i == theCube.get()[DMM] for i in topCorners):
            if theCube.get()[FTL] == theCube.get()[DMM] or theCube.get()[FTR] == theCube.get()[DMM]:
                offset = 0
                F, f, R, r, B, b, L, l, U, u = 'F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u'
            # Right
            elif theCube.get()[RTL] == theCube.get()[DMM] or theCube.get()[RTR] == theCube.get()[DMM]:
                offset = 9
                F, f, R, r, B, b, L, l, U, u = 'R', 'r', 'B', 'b', 'L', 'l', 'F', 'f', 'U', 'u'
            # Back
            elif theCube.get()[BTL] == theCube.get()[DMM] or theCube.get()[BTR] == theCube.get()[DMM]:
                offset = 18
                F, f, R, r, B, b, L, l, U, u = 'B', 'b', 'L', 'l', 'F', 'f', 'R', 'r', 'U', 'u'
            # Orientation
            elif theCube.get()[LTL] == theCube.get()[DMM] or theCube.get()[LTR] == theCube.get()[DMM]:
                offset = 27
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
            
        btmCross = [theCube.get()[DTM], theCube.get()[DMR], theCube.get()[DBM], theCube.get()[DML]]
        if not all(i == theCube.get()[DMM] for i in btmCross):
            solveBottomCross(theCube)