#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_only(self):
        self.assertAlmostEqual(max_integer([1]), 1)
#    def test_str(self):
#        self.assertRaises(TypeError, max_integer([1, 3, 'a', 2]))
