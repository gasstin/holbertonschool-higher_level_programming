#!/usr/bin/python3
# Write a function that adds 2 tuples.


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_add = ()
    tuple_a_aux = ()
    tuple_b_aux = ()
    if len(tuple_a) == 0:
        tuple_a_aux = 0, 0
    elif len(tuple_a) == 1:
        tuple_a_aux = tuple_a[0], 0
    else:
        tuple_a_aux = tuple_a[0], tuple_a[1]

    if len(tuple_b) == 0:
        tuple_b_aux = 0, 0
    elif len(tuple_b) == 1:
        tuple_b_aux = tuple_b[0], 0
    else:
        tuple_b_aux = tuple_b[0], tuple_b[1]

    tuple_add = tuple_a_aux[0] + tuple_b_aux[0], tuple_a_aux[1] + tuple_b_aux[1]
    return(tuple_add)

