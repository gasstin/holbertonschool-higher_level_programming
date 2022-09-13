#!/usr/bin/python3
# Write a function that deletes the item at a specific position in a list.


def delete_at(my_list=[], idx=0):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return (my_list)
        else:
            if idx:
                my_list[:] = my_list[0:idx] + my_list[-(idx - 2):]
            else:
                my_list[:] = my_list[1:len(my_list)]

    return (my_list)
