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
        add = a + b
        return int(add)
    except TypeError:
        if not isinstance(a, int) or not isinstance(a, float):
            return f"a must be an integer"
        if not isinstance(b, int) or not isinstance(b, float):
            return f"b must be an integer"
