#!/usr/bin/python3
"""
    Write the first class Base.
"""
import json


class Base:
    """
        This class will be the “base”
        of all other classes in this project

        The goal of it is to manage id attribute
        in all your future classes and to avoid duplicating
        the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
            returns the JSON string representation of list_dictionaries
        """
        json_s = "[]"
        if list_dictionaries:
            json_s = json.dumps(list_dictionaries)
        return json_s
