#!/usr/bin/python3
# Write a function that prints a matrix of integers.


def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('')
    else:
        for n in range(len(matrix)):
            for m in range(len(matrix)):
                if m < (len(matrix) - 1):
                    print('{:d}'.format(matrix[n][m]), end=' ')
                else:
                    print('{:d}'.format(matrix[n][m]))
