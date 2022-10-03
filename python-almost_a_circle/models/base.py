#!/usr/bin/python3
"""
    Write the first class Base.
"""
import json
import os.path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns the JSON string representation of list_dictionaries
        """
        json_s = "[]"
        if list_dictionaries:
            json_s = json.dumps(list_dictionaries)
        return json_s

    def from_json_string(json_string):
        """
            returns the list of the JSON string representation json_string
        """
        if json_string:
            return json.loads(json_string)
        return list()

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of list_objs to a file:
        """
        if not list_objs:
            return []
        json_s = ""
        if list_objs:
            for list_i in list_objs:
                if list_i != list_objs[0]:
                    json_s += ", "
                json_s += cls.to_json_string(cls.to_dictionary(list_i))
        file_name = cls.__name__ + ".json"
        json_s = "[" + json_s + "]"
        with open(file_name, mode="w", encoding='utf-8') as new_file:
            new_file.write(json_s)

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(5)
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances
        """
        file_name = cls.__name__ + ".json"
        list_final = []
        if os.path.exists(file_name):
            with open(file_name, "r") as my_file:
                list_aux = cls.from_json_string(my_file.read())
                for ll in list_aux:
                    list_final += [cls.create(**ll)]
        return list_final
