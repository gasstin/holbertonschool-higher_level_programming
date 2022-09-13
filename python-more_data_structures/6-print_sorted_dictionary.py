#!/usr/bin/python3
# Write a function that prints a dictionary by ordered keys.


def print_sorted_dictionary(a_dictionary):
    aux_k = []
    aux_v = []
    for k, v in a_dictionary.items():
        aux_k += [k]
        aux_v += [v]
    aux_k = sorted(aux_k)
    for j in range(len(aux_k)):
        p = 0
        for k in a_dictionary:
            if aux_k[j] != k:
                p += 1
            else:
                break
        print("{} : {}".format(aux_k[j], aux_v[p]))
