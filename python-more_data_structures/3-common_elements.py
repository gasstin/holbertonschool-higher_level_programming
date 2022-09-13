#!/usr/bin/python3
# Write a function that returns a set of common elements in two sets.


def common_elements(set_1, set_2):
    if set_1 and set_2:
        common = {x for x in set_1 if x in set_2}
        return (common)
    else:
        return({})
