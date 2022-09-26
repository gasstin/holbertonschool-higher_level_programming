#!/usr/bin/python3
"""
    Write a class MyList that inherits from list:
"""


class MyList(list):
    """
        MyList recives the attributes of list
    """
    def print_sorted(self):
        """
            that prints the list, but sorted (ascending sort)
        """
        for i in self:
            if type(i) is not int:
                raise TypeError('elements of the list should be of type int')
        print(sorted(self))
