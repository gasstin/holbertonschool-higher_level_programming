#!/usr/bin/python3
"""
    Write a class Square that inherits
    from Rectangle (9-rectangle.py):
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle, BaseGeometry):
    """
        This class create a square

        - width and height must be positive integers
        validated by integer_validator
        - the area() method must be implemented
    """
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)
