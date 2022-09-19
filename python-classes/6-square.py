#!/usr/bin/python3
"""Write a class Square that defines a square by:
    based on 5-square.py
"""


class Square:
    """This class creates a square

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): is the size of the square
        """
        self.__set_size(size)
        self.__set_position(position)

    @property
    def __get_size(self):
        return self.size

    def __set_size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.size = value

    def __get_position(self):
        return self.position

    def __set_position(self, value):
        if len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def area(self):
        """Return the area of the square"""
        return (self.__get_size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.size:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
