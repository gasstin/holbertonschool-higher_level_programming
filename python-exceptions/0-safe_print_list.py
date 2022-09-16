#!/usr/bin/python3
# Write a function that prints x elements of a list.


def safe_print_list(my_list=[], x=0):
    try:
        if my_list and x:
            for i in range(x):
                if my_list[i]:
                    print(f"{my_list[i]}", end='')
                    if (i == x-1):
                        print()
                else:
                    break
        return (x)
    except Exception:
            print()
            return (i)
