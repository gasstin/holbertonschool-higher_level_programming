#!/usr/bin/python3
'''
    size is the size length of the square
    size must be an integer, otherwise raise a
    TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError
    exception with the message size must be >= 0
'''


def print_square(size):
    """ Write a function that prints a square with the character #.

        args:
            size: is the size of the matrix
            div: is the divisor number
        Return:
            a square
    """
    if type(size) is not int or type(size) is float:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
