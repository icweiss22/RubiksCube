from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    
    # validation
    if Cube.cubeValidation(None,parms).get('status') != 'ok':
        return Cube.cubeValidation(None,parms)
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    solveBottomCross(theCube)      #iteration 2
    solveBottomLayer(theCube)      #iteration 3
    solveMiddleLayer(theCube)      #iteration 4
    solveUpCross(theCube)          #iteration 5
    solveUpSurface(theCube)        #iteration 5
    solveUpperLayer(theCube)       #iteration 6
    
    cleanSolution(theCube)
    
    result['solution'] = theCube.getSolution()
    result['status'] = 'ok'    
    result['integrity'] = ''       #iteration 6
                     
    return result

def cleanSolution(theCube: Cube):
    mutableList = theCube.getSolution()
    # turn three counterclockwises into a clockwise
    mutableList = mutableList.replace('fff', 'F')
    mutableList = mutableList.replace('fff', 'F')
    mutableList = mutableList.replace('rrr', 'R')
    mutableList = mutableList.replace('bbb', 'B')
    mutableList = mutableList.replace('lll', 'L')
    mutableList = mutableList.replace('uuu', 'U')
    mutableList = mutableList.replace('ddd', 'D')
    # turn three clockwises into a counterclockwise
    mutableList = mutableList.replace('FFF', 'f')
    mutableList = mutableList.replace('RRR', 'r')
    mutableList = mutableList.replace('BBB', 'b')
    mutableList = mutableList.replace('LLL', 'l')
    mutableList = mutableList.replace('UUU', 'u')
    mutableList = mutableList.replace('DDD', 'd')
    # remove consecutive lowercase/uppercase
    for i in range(0, len(mutableList) - 1):
        charOne = mutableList[i]
        charTwo = mutableList[i+1]
        if charOne.lower() == charTwo.lower() and charOne.isupper() != charTwo.isupper(): 
            mutableList = mutableList[:i] + '!!' + mutableList[i+2:]
    mutableList = mutableList.replace('!', '')
    theCube.setSolution(mutableList)
    