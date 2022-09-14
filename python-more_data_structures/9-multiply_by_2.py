#!/usr/bin/python3
# Write a function that returns new dictionary with all values multiplied by 2


def multiply_by_2(a_dictionary):
    new_dict = dict()
    if a_dictionary:
        for k, v in a_dictionary.items():
            v = v * 2
            new_dict[k] = v
    return (new_dict)
