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
    return not issubclass(a_class, type(obj))
