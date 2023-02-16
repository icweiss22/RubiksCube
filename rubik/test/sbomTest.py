'''
Created on Jan 20, 2023

@author: isaacweiss
'''
import unittest
import app


class SbomTest(unittest.TestCase):


    def test_sbom_100_ShouldReturnArthurName(self):
        myName = 'icw0001'
        result = app._getAuthor('../../')
        resultingAuthorName = result['author']
        self.assertEqual(resultingAuthorName, myName)