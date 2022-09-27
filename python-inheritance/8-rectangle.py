#!/usr/bin/python3
"""
    Write a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        This class create a rectangle
    """
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
