#!/usr/bin/python3
"""
    Write a function that returns True if the object is
    an instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
        Args:
            obj: is the object to check.
            a_class: is the class.

        Returns:
                True or False
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
