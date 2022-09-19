#!/usr/bin/python3
"""Write a class Square that defines a square by:
    based on 4-square.py
"""


class Square:
    """This class creates a square

    """
    def __init__(self, size=0):
        """
        Args:
            size (int): is the size of the square
        """
        self.__set_size(size)

    def __get_size(self):
        return self.__size

    def __set_size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
    size = property(__get_size, __set_size)

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
