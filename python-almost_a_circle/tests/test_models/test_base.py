import unittest
from models.base import Base
class Test_Base(unittest.TestCase):
    
    def test_change(self):
        b5 = Base()
        b5.id = 4
        self.assertEqual(b5.id, 4)
    
    def test_creates(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(10)
        self.assertEqual(b2.id, 10)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        self.assertNotEqual(b2.id, 2)