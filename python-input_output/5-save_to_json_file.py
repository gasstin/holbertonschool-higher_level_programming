#!/usr/bin/python3
"""
    Task 4
"""
import json


def save_to_json_file(my_obj, filename):
    """
       Write a function that writes an Object to a text file,
       using a JSON representation:
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        return my_file.write(json.dumps(my_obj))
