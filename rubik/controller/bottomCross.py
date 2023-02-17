from rubik.model.cube import Cube

TwoFront, TwoRight, TwoBack, TwoLeft = 'FF', 'RR', 'BB', 'LL'
U = 'U'
'''
Created on Feb 16, 2023

@author: isaacweiss
'''
def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''  
    bottom_cross = [theCube.get()[46], theCube.get()[48], theCube.get()[50], theCube.get()[52]]
    if any(i != theCube.get()[49] for i in bottom_cross):
        theCube.makeCrossGeneric()
        if theCube.get()[1] != theCube.get()[4]: # Front 
            while True:
                theCube.rotate(U)
                if theCube.get()[1] == theCube.get()[4]:
                    break
            theCube.rotate(TwoFront)
        else:
            theCube.rotate(TwoFront)
            
        if theCube.get()[10] != theCube.get()[13]: # Right
            while True:
                theCube.rotate(U)
                if theCube.get()[10] == theCube.get()[13]:
                    break
            theCube.rotate(TwoRight)
        else:
            theCube.rotate(TwoRight)
            
        if theCube.get()[19] != theCube.get()[22]: # Back
            while True:
                theCube.rotate(U)
                if theCube.get()[19] == theCube.get()[22]:
                    break
            theCube.rotate(TwoBack)
        else:
            theCube.rotate(TwoBack)
            
        
        if theCube.get()[28] != theCube.get()[31]: # Left
            while True:
                theCube.rotate(U)
                if theCube.get()[28] == theCube.get()[31]:
                    break
            theCube.rotate(TwoLeft)
        else:
            theCube.rotate(TwoLeft)
    
    return theCube.getSolution()    


