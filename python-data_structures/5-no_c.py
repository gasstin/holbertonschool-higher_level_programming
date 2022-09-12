#!/usr/bin/python3
# Write a function that removes all characters c and C from a string.

def no_c(my_string):
    new_string = ''
    for n in range(len(my_string)):
        if my_string[n] != 'C' and my_string[n] != 'c':
            new_string += my_string[n]
    return (new_string)
