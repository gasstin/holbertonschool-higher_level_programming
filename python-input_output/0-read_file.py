#!/usr/bin/python3
"""
    Task 0
"""


def read_file(filename=""):
    """
    Write a function that reads a text file (UTF8) and prints it to stdout:
    """
    with open(filename, encoding="utf-8") as my_file_open:
        print(my_file_open.read(), end='')
