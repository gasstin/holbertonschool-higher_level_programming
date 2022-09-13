#!/usr/bin/python3
# Write a function that computes the square value of all integers of a matrix.


def square_matrix_simple(matrix=[]):
    if matrix:
        squares_matrix = []
        for i in range(len(matrix)):
            squares_matrix += [list(map(lambda x: x**2, matrix[i]))]
        return (squares_matrix)
