#!/usr/bin/python3
"""
    Write the class Square that inherits from Rectangle:
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        this class creates a square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Args:
                width (int): is the width of the square
                height (int): is the height of the square
                x: is the x position of the square
                y: is the y position of the square
                id(int): is the identification of square

        """
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y
        self.id = id

    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"
