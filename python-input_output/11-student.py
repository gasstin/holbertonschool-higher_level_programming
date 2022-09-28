#!/usr/bin/python3
"""
    Task 10: Write a class Student that defines a student
"""


class Student:
    """
        Public instance attributes:
            first_name
            last_name
            age
        Public method:
            def to_json(self, attrs=None): that retrieves a dictionary
            representation of a Student instance.
            reload_from_json(self, json): that replaces all attributes
            of the Student instance.

        if attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    """

    def __init__(self, first_name, last_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        self.attrs = attrs
        new_dict = self.__dict__
        aux_dict = dict()
        if self.attrs == []:
            return dict()
        if not self.attrs:
            del new_dict['attrs']
            return new_dict
        else:
            for key in new_dict:
                if key in attrs:
                    aux_dict[key] = new_dict[key]
            return aux_dict

    def reload_from_json(self, json):
        self.__dict__ = json
