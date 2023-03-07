from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
from rubik.model.constants import * # @UnusedWildImport

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    
    # validation
    if Cube.cubeValidation(None,parms).get('status') != 'ok':
        return Cube.cubeValidation(None,parms)
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    frontFace = theCube.get()[0:9]
    rightFace = theCube.get()[9:18]
    backFace = theCube.get()[18:27]
    leftFace = theCube.get()[27:36]
    upFace = theCube.get()[36:45]
    downFace = theCube.get()[45:54]
    
    # already solved
    if (all(i == theCube.get()[FMM] for i in frontFace) and 
        all(i == theCube.get()[RMM] for i in rightFace) and 
        all(i == theCube.get()[BMM] for i in backFace) and
        all(i == theCube.get()[LMM] for i in leftFace) and 
        all(i == theCube.get()[UMM] for i in upFace) and 
        all(i == theCube.get()[DMM] for i in downFace)):
        return 
    
    # middle layer solved
    if (all(i == frontFace[4] for i in frontFace[3:]) and
        all(i == rightFace[4] for i in rightFace[3:]) and
        all(i == backFace[4] for i in backFace[3:]) and
        all(i == leftFace[4] for i in leftFace[3:])):
        return
    
    downMiddle = downFace[4]
    if (all(i == downMiddle for i in downFace)):
        solveMiddleLayer(theCube)
    elif (downFace[1] == downFace[3] == downFace[5] == downFace[7] == downMiddle):
        solveBottomLayer(theCube)
        solveMiddleLayer(theCube)
    elif (upFace[1] == upFace[3] == upFace[5] == upFace[7] == downMiddle):
        solveBottomCross(theCube)
        solveBottomLayer(theCube)
        solveMiddleLayer(theCube)
    else:
        theCube.makeCrossGeneric()
        solveBottomCross(theCube)
        solveBottomLayer(theCube)
        solveMiddleLayer(theCube)
    
    cleanSolution(theCube)
    
    result['solution'] = theCube.getSolution()
    result['status'] = 'ok'    
    result['integrity'] = ''       
                     
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
    