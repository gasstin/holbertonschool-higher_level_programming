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

    if not div:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if not len(matrix[0]):
        raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same \
size")
        for index in row:
            if type(index) is not int and type(index) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
    new_m = []
    for i in range(len(matrix)):
        new_m += [list(map(lambda x: round((x / div), 2), matrix[i]))]
    return new_m

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
