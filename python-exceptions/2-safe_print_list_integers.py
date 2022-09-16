#!/usr/bin/python3
# Write a function that prints the first x elements of a list and only integers.


def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for n in range(x):
            if isinstance(my_list[n], int):
                print(f"{my_list[n]:d}", end ='')
                count += 1
            else:
                continue
        print()
    except IndexError:
        raise
        
    return (count)
