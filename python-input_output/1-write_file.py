#!/usr/bin/python3
"""
    Task 1
"""


def write_file(filename="", text=""):
    """
        Write a function that writes a string to a text file (UTF8)
        and returns the number of characters written:
    """
    with open(filename, mode="w", encoding="utf-8") as my_file_open:
        return my_file_open.write(text)
