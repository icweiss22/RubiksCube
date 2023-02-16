from unittest import TestCase
from rubik.view.solve import solve
# below are for testing controller methods
import rubik.model.cube as cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer

class SolveTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
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
    
    # controller methods
    def test_makeBackCrossScrambled(self):
        myCube = cube.Cube('ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro')
        solveBottomCross(myCube)
        back_cross = [myCube.get()[46], myCube.get()[48], myCube.get()[50], myCube.get()[52]]  
        self.assertTrue(all(i == myCube.get()[49] for i in back_cross))
        
    def test_makeBackCrossScrambled2(self):
        myCube = cube.Cube('wyrobwgwoybbbrrwyyorbwgooogywbgobryrogwoyrrbbwgggwryyg')
        solveBottomCross(myCube)
        back_cross = [myCube.get()[46], myCube.get()[48], myCube.get()[50], myCube.get()[52]]  
        self.assertTrue(all(i == myCube.get()[49] for i in back_cross))
        
    def test_makeBackCrossAlreadyDone(self):
        myCube = cube.Cube('worrbbbbobygyrgwrgogyogbrgyoyroobroobryryggywwwgwwwbwy')
        solveBottomCross(myCube)
        self.assertEqual(myCube.getSolution(), '')
