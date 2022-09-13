#!/usr/bin/python3
# Write a function that returns the number of keys in a dictionary.


def number_keys(a_dictionary):
    n_k = 0
    if a_dictionary:
        for key in a_dictionary:
            n_k += 1

    return (n_k)
