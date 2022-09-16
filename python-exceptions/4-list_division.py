#!/usr/bin/python3
# Write a function that divides element by element 2 lists.


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for n in range(list_length):
        try:
            new_list += [my_list_1[n] / my_list_2[n]]
        except TypeError:
            print("wrong type")
            new_list += [0]
            continue
        except ZeroDivisionError:
            print("division by 0")
            new_list += [0]
            continue
        except IndexError:
            print("out of range")
            new_list += [0]
            continue
        finally:
            pass

    return(new_list)
