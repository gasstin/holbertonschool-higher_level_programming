#!/usr/bin/python3
"""
    Write a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        This class create a rectangle

        - width and height must be positive integers
        validated by integer_validator
        - the area() method must be implemented
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
