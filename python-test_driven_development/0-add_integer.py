#!/usr/bin/python3
'''Write a function that adds 2 integers.

    a and b must be integers or floats, otherwise
    raise a TypeError exception with the message
    a must be an integer or b must be an integer.

    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
        '''


def add_integer(a, b=98):
    """ a function that adds 2 integers

        args:
            a: is the first integer
            b: is the second integer
        Return:
            the addition of a and b
    """
    try:
        return int(a + b)
    except TypeError:
        if b is None or (type(b) is not int and type(b) is not float):
            return 'b must be an integer'
        if a is None or (type(a) is not int and type(a) is not float):
            return 'a must be an integer'

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
