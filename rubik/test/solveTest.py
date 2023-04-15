from unittest import TestCase
from rubik.view.solve import solve
# below are for testing controller methods
import rubik.model.cube as cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer, solveUpperCorners
from rubik.model.constants import *  # @UnusedWildImport

class SolveTest(TestCase):
    
    
    '''
    def test_solveSolution(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('FRBLUD', result.get('solution'))
    '''
    def test_missingCube(self):
        parms = {}
        result = solve(parms)
        self.assertNotEqual('ok', result.get('status'))
    def test_cubeIsValidated(self):
        parms = {}
        result = solve(parms)
        self.assertNotEqual('ok', result.get('status'))
        
    def test_cubeAlreadyDone(self):
        cubeStr = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        result = solve({'cube': cubeStr})
        myCube = cube.Cube(cubeStr)
        myCube.rotate(result['solution'])
        self.assertEqual(myCube.getSolution(), '')
    '''
    Bottom cross
    '''
    def test_makeBottomCrossScrambled(self):
        cubeStr = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        myCube = cube.Cube(cubeStr)
        solveBottomCross(myCube)
        bottomCross = [myCube.get()[46], myCube.get()[48], myCube.get()[50], myCube.get()[52]]  
        self.assertTrue(all(i == myCube.get()[49] for i in bottomCross))
    '''
    Bottom layer
    ''' 
    def test_makeBottomLayerScrambled(self):
        cubeStr = 'gbwrryrrobroggyyggyoyoogoogbrwobgrbbrbgyybryowwbwwwyww'
        myCube = cube.Cube(cubeStr)
        solveBottomCross(myCube)
        solveBottomLayer(myCube)
        bottomLayer = myCube.get()[45:54]
        self.assertTrue(all(i == myCube.get()[49] for i in bottomLayer))
    def test_makeBottomLayerScrambled2(self):
        cubeStr = 'wrybbwygobgwrrwybbgygbgywbowrbgoogoroorgywryrgobwwyyro'
        myCube = cube.Cube(cubeStr)
        solveBottomCross(myCube)
        solveBottomLayer(myCube)
        bottomLayer = myCube.get()[45:54]
        self.assertTrue(all(i == myCube.get()[49] for i in bottomLayer))
    '''
    Middle layer
    ''' 
    def test_makeMiddleLayerScrambled(self):
        cubeStr = 'gbwrryrrobroggyyggyoyoogoogbrwobgrbbrbgyybryowwbwwwyww'
        theCube = cube.Cube(cubeStr)
        solveBottomCross(theCube)
        solveBottomLayer(theCube)
        solveMiddleLayer(theCube)
        frontMiddleLayer = theCube.get()[3:9]
        rightMiddleLayer = theCube.get()[12:18]
        backMiddleLayer = theCube.get()[21:27]
        leftMiddleLayer = theCube.get()[30:36]
        self.assertTrue(all(i == theCube.get()[4] for i in frontMiddleLayer))
        self.assertTrue(all(i == theCube.get()[13] for i in rightMiddleLayer))
        self.assertTrue(all(i == theCube.get()[22] for i in backMiddleLayer))
        self.assertTrue(all(i == theCube.get()[31] for i in leftMiddleLayer))
    
    def test_makeMiddleLayerScrambled2(self):
        cubeStr = 'wrybbwygobgwrrwybbgygbgywbowrbgoogoroorgywryrgobwwyyro'
        myCube = cube.Cube(cubeStr)
        solveBottomCross(myCube)
        solveBottomLayer(myCube)
        solveMiddleLayer(myCube)
        frontMiddleLayer = myCube.get()[3:9]
        rightMiddleLayer = myCube.get()[12:18]
        backMiddleLayer = myCube.get()[21:27]
        leftMiddleLayer = myCube.get()[30:36]
        self.assertTrue(all(i == myCube.get()[4] for i in frontMiddleLayer))
        self.assertTrue(all(i == myCube.get()[13] for i in rightMiddleLayer))
        self.assertTrue(all(i == myCube.get()[22] for i in backMiddleLayer))
        self.assertTrue(all(i == myCube.get()[31] for i in leftMiddleLayer))
    '''
    Up Cross/Surface
    '''
    def test_makeUpCrossScrambled(self):
        cubeStr = 'gbwrryrrobroggyyggyoyoogoogbrwobgrbbrbgyybryowwbwwwyww'
        myCube = cube.Cube(cubeStr)
        solveBottomCross(myCube)
        solveBottomLayer(myCube)
        solveMiddleLayer(myCube)
        solveUpCross(myCube)
        self.assertTrue(all(myCube.get()[UMM] == myCube.get()[i] for i in [UML,UMR,UTM,UBM]))
        
    def test_makeUpCrossScrambled2(self):
        cubeStr = 'wrybbwygobgwrrwybbgygbgywbowrbgoogoroorgywryrgobwwyyro'
        myCube = cube.Cube(cubeStr)
        solveBottomCross(myCube)
        solveBottomLayer(myCube)
        solveMiddleLayer(myCube)
        solveUpCross(myCube)
        self.assertTrue(all(myCube.get()[UMM] == myCube.get()[i] for i in [UML,UMR,UTM,UBM]))
    def test_makeUpSurfaceScrambled(self):
        cubeStr = 'gbwrryrrobroggyyggyoyoogoogbrwobgrbbrbgyybryowwbwwwyww'
        myCube = cube.Cube(cubeStr)
        solveBottomCross(myCube)
        solveBottomLayer(myCube)
        solveMiddleLayer(myCube)
        solveUpCross(myCube)
        solveUpSurface(myCube)
        upSurface = myCube.get()[36:44]
        self.assertTrue(len(set(upSurface)) == 1)
    def test_makeUpSurfaceScrambled2(self):
        cubeStr = 'ygbbbbbbbybgrrrrrryogggggggorrooooooyyryyybyowwwwwwwww'
        myCube = cube.Cube(cubeStr)
        solveBottomCross(myCube)
        solveBottomLayer(myCube)
        solveMiddleLayer(myCube)
        solveUpCross(myCube)
        solveUpSurface(myCube)
        upSurface = myCube.get()[36:44]
        self.assertTrue(len(set(upSurface)) == 1)
    def test_makeUpSurfaceScrambled3(self):
        cubeStr = 'wbborboorwgowgggygwgyrowrororgrbybgybybyyworrgwwowbyby'
        myCube = cube.Cube(cubeStr)
        solveBottomCross(myCube)
        solveBottomLayer(myCube)
        solveMiddleLayer(myCube)
        solveUpCross(myCube)
        solveUpSurface(myCube)
        upSurface = myCube.get()[36:44]
        self.assertTrue(len(set(upSurface)) == 1)
    '''
    Up Layer
    '''
    def test_makeUpperLayerScrambed(self):
        cubeStr = 'gogggggggorooooooobbbbbbbbbrgrrrrrrryyyyyyyyywwwwwwwww'
        myCube = cube.Cube(cubeStr)
        solveUpperLayer(myCube)
        print(myCube.get())
        self.assertTrue(len(set(myCube.get()[0:9])) == 1)
        self.assertTrue(len(set(myCube.get()[9:18])) == 1)
        self.assertTrue(len(set(myCube.get()[18:27])) == 1)
        self.assertTrue(len(set(myCube.get()[27:36])) == 1)
        self.assertTrue(len(set(myCube.get()[36:45])) == 1)
        self.assertTrue(len(set(myCube.get()[45:54])) == 1)
        
    def test_makeUpperLayerScrambed2(self):
        cubeStr = 'brgrrrrrroobggggggrgroooooogbobbbbbbyyyyyyyyywwwwwwwww'
        result = solve({'cube': cubeStr})
        myCube = cube.Cube(result['newCube'])
        self.assertTrue(len(set(myCube.get()[0:9])) == 1)
        self.assertTrue(len(set(myCube.get()[9:18])) == 1)
        self.assertTrue(len(set(myCube.get()[18:27])) == 1)
        self.assertTrue(len(set(myCube.get()[27:36])) == 1)
        self.assertTrue(len(set(myCube.get()[36:45])) == 1)
        self.assertTrue(len(set(myCube.get()[45:54])) == 1)
    '''
    Complete Tests 
    '''
    def test_solveRubiksCube(self):
        cubeStrings = ['yywwroborobbbggwwrygyyoygyyboobbbggorrowyrgogwgbwwrrrw','ygoyrrowbwrbggboowrrooobbogywgybgwgggyyrybrwbwbyowwryr', 
                       'gbyorworybowrggbywgbgworbwrooogbgyywyrrbyywwrbyogwbgor', 'wrggrywwwyrrrgyoogyorbooywbwwgybwogrgbbrybogrbbbywgyoo',
                       'yyogryybwgowbgybrbgwroowwryggbbbwrggyorrygorwoorywbbwo', 'wbybrwyoyobyogworwbowrobbywowoyboryrggrgywbrbgygrwgggr',
                       'yrwyrowoygbbwgwgoborogoryyygybwboogrwywbywobrbgrrwbggr', 'orrwrgwrygoyrgyrwwobwgoorbyrobybbooobrbwybwyygwbgwggyg']

        for i in cubeStrings:
            solve({'cube': i})['newCube']
            
    def test_specificTest(self):
        print(solve({'cube': 'f6zzoo6fxofr666zorxozfrofrr6rxxxrxxorzzxzxoz6frozfff66'})['newCube'])
        