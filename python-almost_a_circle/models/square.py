#!/usr/bin/python3
"""
    Write the class Square that inherits from Rectangle:
"""
from models.base import Base
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
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(self.size, self.size, self.x, self.y, self.id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
