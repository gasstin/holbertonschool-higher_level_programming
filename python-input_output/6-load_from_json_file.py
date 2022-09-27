#!/usr/bin/python3
"""
    Task 6
"""
import json


def load_from_json_file(filename):
    """
      Write a function that creates an Object from a “JSON file”:
    """
    with open(filename, mode='r', encoding='utf-8') as my_file:
        return json.load(my_file)
