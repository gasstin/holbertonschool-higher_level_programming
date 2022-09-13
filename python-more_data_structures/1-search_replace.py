#!/usr/bin/python3
# Write a function that replaces all occurrences
# of an element by another in a new list.


def search_replace(my_list, search, replace):
    if my_list:
        aux_list = []
        aux_list += list(map(lambda x: replace if x == search else x, my_list))
        return (aux_list)
    return([])
