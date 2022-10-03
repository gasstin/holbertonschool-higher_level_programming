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
            Rectangle(4, "b")
        with self.assertRaises(TypeError):
            Rectangle("b", 2)
        with self.assertRaises(TypeError):
            Rectangle(4, 2, "a", 0, 20)
        with self.assertRaises(TypeError):
            Rectangle(4, 2, 0, "b", 20)
        with self.assertRaises(TypeError):
            Rectangle()
    
    def test_raise_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 0, 0, 20)
        with self.assertRaises(ValueError):
            Rectangle(4, 0, 0, 0, 20)
        with self.assertRaises(ValueError):
            Rectangle(-4, 2, 0, 0, 20)
        with self.assertRaises(ValueError):
            Rectangle(4, 2, -2, 0, 20)
        with self.assertRaises(ValueError):
            Rectangle(4, 3, 0, -2, 20)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
    
    def test_display(self):
        r1 = Rectangle(2, 2)
        r1.display()
        with self.assertRaises(TypeError):
            Rectangle.display()
    
    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 0, 0, 20)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'height': 2, 'id': 20, 'width': 10, 'x': 0, 'y': 0})
    
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
    
    def test_update(self):
        r1 = Rectangle(5, 5, 5, 5, 5)
        r1.update(89, 2, 3, 4, 6)
        self.assertEqual(r1.id, 89)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.x, 1)
        