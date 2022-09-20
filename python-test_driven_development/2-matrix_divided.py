#!/usr/bin/python3
'''Write a function that divides all elements of a matrix.
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message
    matrix must be a matrix (list of lists) of integers/floats
    Returns a new matrix
'''


def matrix_divided(matrix, div):
    """ a function that adds 2 integers
        args:
            matrix: is the matrix to divide
            div: is the divisor number
        Return:
            the new matrix
    """
    try:
        if not div:
             raise ZeroDivisionError('division by zero')
        new_m = []
        for i in range(len(matrix)):
            new_m += [list(map(lambda x: round((x / div), 2), matrix[i]))]
        return new_m
    except TypeError:
        if type(matrix[i]) is not int and type(matrix[i]) is not float:
            return 'matrix must be a matrix (list of lists) of integers/floats'
        if len(matrix[i]) != len(matrix[i]):
            return 'Each row of the matrix must have the same size'
        if type(div) is not int and type(div) is not float:
            print('div must be a number')
        return None

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
