import unittest
from models.rectangle import Rectangle
class Test_Base(unittest.TestCase):
    
    def test_check_position(self):
        r2 = Rectangle(4, 2, 0, 0, 20)
        self.assertEqual(r2.x, 0)
        self.assertNotEqual(r2.y, 1)

    def test_creates(self):
        r1 = Rectangle(10,2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(4, 2, 0, 0, 20)
        self.assertEqual(r2.id, 20)
    
    def test_raise_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 2, "a", 0, 20)
    
    def test_raise_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 0, 0, 0, 20)
        with self.assertRaises(ValueError):
            Rectangle(4, 3, 0, -2, 20)
    
    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)