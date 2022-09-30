import unittest
from models.square import Square
class Test_Base(unittest.TestCase):
    

    def test_creates_square(self):
        s3 = Square(3, 1, 3)
        print(s3)
        print(s3.area())
        s3.display()

    def test_raise_value_error_square(self):
        with self.assertRaises(ValueError):
            Square(0, 1, 3)
    
    def test_raise_type_error_square(self):
        s1 = Square(5)
        with self.assertRaises(TypeError):
            s1.size = "9"
           
    
