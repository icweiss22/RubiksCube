from unittest import TestCase
from rubik.view.solve import solve
# below are for testing controller methods
import rubik.model.cube as cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer

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
    
    def test_cubeIsValidated(self):
        parms = {'cube': 'xxx'}
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
        solveBottomLayer(myCube)
        bottomLayer = myCube.get()[45:54]
        self.assertTrue(all(i == myCube.get()[49] for i in bottomLayer))
    '''
    Middle layer
    ''' 
    def test_makeMiddleLayerScrambled(self):
        cubeStr = 'gbwrryrrobroggyyggyoyoogoogbrwobgrbbrbgyybryowwbwwwyww'
        myCube = cube.Cube(cubeStr)
        solveMiddleLayer(myCube)
        frontMiddleLayer = myCube.get()[3:9]
        rightMiddleLayer = myCube.get()[12:18]
        backMiddleLayer = myCube.get()[21:27]
        leftMiddleLayer = myCube.get()[30:36]
        self.assertTrue(all(i == myCube.get()[4] for i in frontMiddleLayer))
        self.assertTrue(all(i == myCube.get()[13] for i in rightMiddleLayer))
        self.assertTrue(all(i == myCube.get()[22] for i in backMiddleLayer))
        self.assertTrue(all(i == myCube.get()[31] for i in leftMiddleLayer))
        
    