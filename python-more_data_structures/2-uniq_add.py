#!/usr/bin/python3
# Write a function that adds all unique integers
# in a list (only once for each integer).


def uniq_add(my_list=[]):
    sumt = 0
    if my_list:
        my_list.sort()
        for n in range(len(my_list)):
            if n < (len(my_list) - 1):
                if my_list[n] != my_list[n + 1]:
                    sumt += my_list[n]
            else:
                sumt += my_list[n]
    return (sumt)
