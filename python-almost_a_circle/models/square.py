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
        self.width = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(self.width, self.width, self.x, self.y, self.id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
            update the values of a square.
        """
        if args:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v
                if k == 'size':
                    self.width = v
                    self.size = v
                if k == 'id':
                    self.id = v
