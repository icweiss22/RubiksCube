from rubik.model.constants import * # @UnusedWildImport
from rubik.model.cube import Cube
from rubik.controller.bottomLayer import solveBottomLayer

F, f, R, r, B, b, L, l, U, u, D, d = 'F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd'
def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    '''  
    while any(color != theCube.get()[4] for color in [theCube.get()[3], theCube.get()[4], theCube.get()[5]]) or any(color != theCube.get()[13] for color in [theCube.get()[12], theCube.get()[13], theCube.get()[14]]) or any(color != theCube.get()[22] for color in [theCube.get()[21], theCube.get()[22], theCube.get()[23]]) or any(color != theCube.get()[31] for color in [theCube.get()[30], theCube.get()[31], theCube.get()[32]]):
        if theCube.get()[1] != theCube.get()[40] and theCube.get()[43] != theCube.get()[40]:
            if theCube.get()[1] == theCube.get()[4]:
                if theCube.get()[43] == theCube.get()[31]:
                    theCube.rotate(u + l + u + L)
                elif theCube.get()[43] == theCube.get()[13]:
                    theCube.rotate(U + R + U + r)
            elif theCube.get()[1] == theCube.get()[13]:
                theCube.rotate(u)
                if theCube.get()[41] == theCube.get()[4]:
                    theCube.rotate(u + f + u + F)
                elif theCube.get()[41] == theCube.get()[22]:
                    theCube.rotate(U + B + U + b)
            elif theCube.get()[1] == theCube.get()[22]:
                theCube.rotate(u + u)
                if theCube.get()[37] == theCube.get()[13]:
                    theCube.rotate(u + r + u + R)
                elif theCube.get()[37] == theCube.get()[31]:
                    theCube.rotate(U + L + U + l)
            elif theCube.get()[1] == theCube.get()[31]:
                theCube.rotate(U)
                if theCube.get()[39] == theCube.get()[22]:
                    theCube.rotate(u + b + u + B)
                elif theCube.get()[39] == theCube.get()[4]:
                    theCube.rotate(U + F + U + f)
            # fix down face
            solveBottomLayer(theCube)
        # flipped condition
        else:
            if theCube.get()[5] == theCube.get()[13]:
                theCube.rotate(R + U + r)
            elif theCube.get()[12] == theCube.get()[4]:
                theCube.rotate(f + u + F)
            elif theCube.get()[14] == theCube.get()[22]:
                theCube.rotate(B + U + b)
            elif theCube.get()[21] == theCube.get()[13]:
                theCube.rotate(r + u + R)
            elif theCube.get()[23] == theCube.get()[31]:
                theCube.rotate(L + U + l)
            elif theCube.get()[30] == theCube.get()[22]:
                theCube.rotate(b + u + B)
            elif theCube.get()[32] == theCube.get()[4]:
                theCube.rotate(F + U + f)
            elif theCube.get()[3] == theCube.get()[31]:
                theCube.rotate(l + u + L)
            solveBottomLayer(theCube)
            theCube.rotate(U)
