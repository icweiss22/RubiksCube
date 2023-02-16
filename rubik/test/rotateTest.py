'''
Created on Jan 25, 2023

@author: isaacweiss
'''
from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
# Happy path
#    Test that the stubbed rotate returns the correct result
    def test_greenLight(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual('bbbbbbbbbyrryrryrroooooooooggwggwggwyyyyyygggrrrwwwwww', result.get('cube'))
        
    def test_noCube(self):
        parms = {'dir': 'F'}
        result = rotate(parms)
        self.assertNotEqual('ok', result['status'], result['status'])
        
    def test_noDirection(self):
        parms = {'cube': 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'}
        result = rotate(parms)
        self.assertEqual('ok', result['status'])
        
    def test_invalidDirectionChar(self):
        parms = {'cube': 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww', 'dir': 'X'}
        result = rotate(parms)
        self.assertNotEqual('ok', result['status'], result['status'])
        
    def test_cubeNotAlphaNum(self):
        parms = {'cube': 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwww&'}
        result = rotate(parms)
        self.assertNotEqual('ok', result['status'], result['status'])
        
    def test_cubeNot54Chars(self):
        parms = {'cube': 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwwww'}
        result = rotate(parms)
        self.assertNotEqual('ok', result['status'], result['status'])
        
    def test_cubeNotUniqueCenters(self):
        parms = {'cube': 'bbbbrbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww', 'dir': 'FfRr'}
        result = rotate(parms)
        self.assertNotEqual('ok', result['status'], result['status'])
        
    def test_cubeNotSixColors(self):
        parms = {'cube': 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwvw'}
        result = rotate(parms)
        self.assertNotEqual('ok', result['status'], result['status'])
        
