#!/usr/bin/python3
# Write a function that replaces or adds key/value in a dictionary.


def update_dictionary(a_dictionary, key, value):
    new_key = {key: value}
    a_dictionary.update(new_key)
    return (a_dictionary)
