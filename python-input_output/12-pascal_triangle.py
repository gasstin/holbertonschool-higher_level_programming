#!/usr/bin/python3
"""
    Task 12
"""


def pascal_triangle(n):
    """
        Create a function pascal_triangle():
        that returns a list of lists of integers representing
        the Pascal triangle of n
    """
    pascal_list = []
    if n > 0:
        pascal_list = [[] for i in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if j == 0:
                    pascal_list[i].append(1)
                elif j == i:
                    pascal_list[i].append(1)
                else:
                    pascal_list[i].append(pascal_list[i - 1][j] +
                                          pascal_list[i - 1][j - 1])
    return pascal_list
