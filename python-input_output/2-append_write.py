#!/usr/bin/python3
"""
    Task 2
"""


def append_write(filename="", text=""):
    """
        Write a function that appends a string at the end of a text file
        (UTF8) and returns the number of characters added:
    """

    with open(filename, mode='a', encoding="utf-8") as my_file:
        return my_file.write(text)
