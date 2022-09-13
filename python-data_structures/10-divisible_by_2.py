#!/usr/bin/python3
# Write a function that finds all multiples of 2 in a list.


def divisible_by_2(my_list=[]):
    if my_list:
        list_result = []
        for n in range(len(my_list)):
            if my_list[n] % 2:
                list_result = list_result + [0]
            else:
                list_result = list_result + [1]
        return (list_result)
