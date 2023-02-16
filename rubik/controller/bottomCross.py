from rubik.model.cube import Cube

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
    if any(i != theCube.get()[49] for i in bottom_cross): # bottom cross not yet solved
        theCube._makeCrossGeneric()
        if theCube.get()[1] != theCube.get()[4]: #front 
            while True:
                theCube.rotate('U')
                if theCube.get()[1] == theCube.get()[4]:
                    break
            theCube.rotate('FF')
        else:
            theCube.rotate('FF')
            
        if theCube.get()[10] != theCube.get()[13]: #right
            while True:
                theCube.rotate('U')
                if theCube.get()[10] == theCube.get()[13]:
                    break
            theCube.rotate('RR')
        else:
            theCube.rotate('RR')
            
        if theCube.get()[19] != theCube.get()[22]: #back
            while True:
                theCube.rotate('U')
                if theCube.get()[19] == theCube.get()[22]:
                    break
            theCube.rotate('BB')
        else:
            theCube.rotate('BB')
            
        
        if theCube.get()[28] != theCube.get()[31]: #left
            while True:
                theCube.rotate('U')
                if theCube.get()[28] == theCube.get()[31]:
                    break
            theCube.rotate('LL')
        else:
            theCube.rotate('LL')
    
    return theCube.getSolution()    


