#!/usr/bin/python3
"""
    Write a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py).
"""


class BaseGeometry:
    """
        This is a geometry class.

        Public instance method: area.
        Public instance method: integer_validator - that validates value:
    """  
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
        return 


class Rectangle(BaseGeometry):
    """
        This class create a rectangle
    """
    def __init__(self, width, height):
        self.__width = BaseGeometry.integer_validator(Rectangle, "width", width)
        self.__height = BaseGeometry.integer_validator(Rectangle, "height", height)
    #    self.__width = super().integer_validator("width", width)
    #    self.__height = super().integer_validator("height", height)