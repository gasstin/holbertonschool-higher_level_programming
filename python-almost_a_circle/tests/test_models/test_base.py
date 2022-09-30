import unittest
from models.base import Base
class Test_Base(unittest.TestCase):
    def test_creates(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(10)
        self.assertEqual(b2.id, 10)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        self.assertNotEqual(b2.id, 2)