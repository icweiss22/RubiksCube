from unittest import TestCase
from rubik.view.solve import solve
# below are for testing controller methods
import rubik.model.cube as cube

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
    Back cross
    '''
    def test_makeDownCrossScrambled(self):
        cubeStr = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        result = solve({'cube': cubeStr})
        myCube = cube.Cube(cubeStr)
        myCube.rotate(result['solution'])
        backCross = [myCube.get()[46], myCube.get()[48], myCube.get()[50], myCube.get()[52]]  
        print(result['solution'])
        self.assertTrue(all(i == myCube.get()[49] for i in backCross))
        
    '''
    Down layer
    ''' 
    def test_makeDownLayerScrambled2(self):
        cubeStr = 'gbwrryrrobroggyyggyoyoogoogbrwobgrbbrbgyybryowwbwwwyww'
        result = solve({'cube': cubeStr})
        myCube = cube.Cube(cubeStr)
        myCube.rotate(result['solution'])
        backFace = myCube.get()[45:54]
        self.assertTrue(all(i == myCube.get()[49] for i in backFace))
    