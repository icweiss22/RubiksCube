from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
from rubik.model.constants import * # @UnusedWildImport
import hashlib

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}

    # validation
    cubeStr = parms.get('cube')
    if not(cubeStr is None):
        theCube = Cube(cubeStr)
    else:
        result['status'] = 'error: cube is required'
        return result
    
    validationMessage = theCube.cubeValidation()
    if validationMessage != 'ok':
        result['status'] = validationMessage
        return result
    
    result['status'] = validationMessage
    result['solution'] = ''
    result['integrity'] = ''
    
    solveBottomCross(theCube)
    
    solveBottomLayer(theCube)
    
    solveMiddleLayer(theCube)
    
    solveUpCross(theCube)
    
    solveUpSurface(theCube)
    
    solveUpperLayer(theCube)
        
    cleanSolution(theCube)
    result['solution'] = theCube.getSolution()

    itemToTokenize = theCube.getSolution() + cubeStr + 'icw0001'
    sha256Hash = hashlib.sha256()
    sha256Hash.update(itemToTokenize.encode())
    fullToken = sha256Hash.hexdigest()
    result['integrity'] = fullToken
    result['newCube'] = theCube.get() # for testing purposes
    
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
    