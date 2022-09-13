#!/usr/bin/python3
# Write a function that finds the biggest integer of a list.


def max_integer(my_list=[]):
    if my_list:
        max_list = my_list[0]
        for n in range(1, len(my_list)):
            if my_list[n] > max_list:
                max_list = my_list[n]
    else:
        max_list = None

    return (max_list)
