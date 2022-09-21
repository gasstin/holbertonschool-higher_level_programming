#!/usr/bin/python3
"""
    Write a class Rectangle that defines a rectangle by:
    (based on 0-rectangle.py)

"""


class Rectangle:
    """
        this class define a real rectangle

    """
    def __init__(self, width=0, height=0):
        """
            Args:
                width (int): is the width of the rectangle
                height (int): is the height of the rectangle

        """
        self.height = height
        self.width = width

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
