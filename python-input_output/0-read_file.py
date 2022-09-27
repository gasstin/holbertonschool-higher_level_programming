#!/usr/bin/python3
"""
    Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    with open("my_file_text_0.txt", encoding="utf-8") as my_file_open:
        print(my_file_open.read())
