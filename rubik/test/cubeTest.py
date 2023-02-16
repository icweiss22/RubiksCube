'''
Created on Jan 25, 2023

@author: isaacweiss
'''
import unittest
import rubik.model.cube as cube


class CubeTest(unittest.TestCase):


    def test_rotateF(self):
        preRotateCube = cube.Cube('wbgobwoyrywygroggroroygrbbwgrbyobowywbbgyorwrggwrwobyy')
        postRotateCube = preRotateCube.rotate('F')
        self.assertEqual(postRotateCube, 'oowybbrwgrwywrorgroroygrbbwgrgyogowwwbbgyoybbggyrwobyy')
        