#!/usr/bin/python3
"""
    Write a class BaseGeometry (based on 5-base_geometry.py).
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
            raise ValueError(f'{name} must be great than 0')
