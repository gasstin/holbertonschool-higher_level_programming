#!/usr/bin/python3
"""
    Write a function that returns the list
    of available attributes and methods of an object:
"""


def lookup(obj):
    """
        Args:
            obj: os the object to look.

        Returns:
                a list object
    """
    return dir(obj)
