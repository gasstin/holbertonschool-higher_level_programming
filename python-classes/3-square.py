#!/usr/bin/python3
"""Write a class Square that defines a square by:
    based on 2-square.py
"""


class Square:
    """This class creates a square

    """
    def __init__(self, size=0):
        """
        Args:
            size (int): is the size of the square
        """
        self.set_size(size)

    def set_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)
