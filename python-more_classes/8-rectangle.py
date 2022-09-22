#!/usr/bin/python3
"""
    Write a class Rectangle that defines a rectangle by:
    (based on 7-rectangle.py)

"""


class Rectangle:
    """
        this class define a real rectangle

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Args:
                width (int): is the width of the rectangle
                height (int): is the height of the rectangle

        """
        self.height = height
        self.width = width

        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if not self.height or not self.width:
            return 0
        return (2 * (self.height + self.width))

    def __str__(self):
        if not self.height or not self.width:
            return ""
        s = ''
        for i in range(self.height):
            for j in range(self.width):
                s += str(self.print_symbol)
            s += "\n"
        return s[:-1]

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2
