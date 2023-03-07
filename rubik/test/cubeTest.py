'''
Created on Jan 25, 2023

@author: isaacweiss
'''
import unittest
import rubik.model.cube as cube

class CubeTest(unittest.TestCase):

    def test_rotateF(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('F'), 'oowybbrwgrwywrorgroroygrbbwgrgyogowwwbbgyoybbggyrwobyy')
        
    def test_rotatef(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('f'), 'gwrbbywoowwygroggroroygrbbwgrryowowrwbbgyoyggbbyrwobyy')

    def test_rotateR(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('R'), 'wbwobooyyggygrwroyrroogrbbwgrbyobowywbggywrwrggbrwybyo')
        
    def test_rotater(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('r'), 'wbbobooyryorwrgyggyroogrwbwgrbyobowywbbgyyrwogggrwwbyr')

    def test_rotateB(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('B'), 'wbgobwoyrywygryggbbyobgrwrobrbbobwwyyorgyorwrggwrwogyo')
        
    def test_rotateb(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('b'), 'wbgobwoyrywwgrbggborwrgboybbrbyobywyoyggyorwrggwrworoy')

    def test_rotateL(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('L'), 'wbggbwryrywygroggrorbygrbbgoygworybbwbbryoowrwgwowooyy')
        
    def test_rotatel(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('l'), 'gbgrbwbyrywygroggrorryggbbwbbyrowgyowbboyoowrwgwrwooyy')

    def test_rotateU(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('U'), 'ywyobwoyrorogroggrgrbygrbbwwbgyobowyrgwwybrobggwrwobyy')
        
    def test_rotateu(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('u'), 'grbobwoyrwbggroggrywyygrbbworoyobowyborbywwgrggwrwobyy')
    
    def test_rotateMultipleRotationsBackToStart(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('FfRrBbLlUu'), 'wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')

    def test_rotateMultipleRotations(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        self.assertEqual(preRotateCube.rotate('FrBlU'), 'yogrbogwbyoywryrwbggwbggwrrgobrowbbwryobygoyrogwrwbyyo')