#!/usr/bin/python3
# Write a function that returns a key with the biggest integer value.


def best_score(a_dictionary):
    maxi = None
    if a_dictionary:
        maxi = max(a_dictionary, key=lambda x: a_dictionary[x])
    return (maxi)
