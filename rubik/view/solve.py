from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
import rubik.view.rotate as rotate

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    
    # validation
    if rotate.cubeValidation(parms).get('status') != 'ok':
        return rotate.cubeValidation(parms)
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    solveBottomCross(theCube)      #iteration 2
    solveBottomLayer(theCube)      #iteration 3
    solveMiddleLayer(theCube)      #iteration 4
    solveUpCross(theCube)          #iteration 5
    solveUpSurface(theCube)        #iteration 5
    solveUpperLayer(theCube)       #iteration 6
    
    result['solution'] = theCube.getSolution()
    result['status'] = 'ok'    
    result['integrity'] = ''       #iteration 3
                     
    return result