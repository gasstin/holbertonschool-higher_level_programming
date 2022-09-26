#!/usr/bin/python3
"""
    Write a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
        Args:
            obj: os the object to check.
            a_class: is the class to check

        Returns:
                True or False
    """
#    if isinstance(type(obj), a_class):
#        return False
    return type(obj) is a_class
