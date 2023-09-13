#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()
    list_k = list(new_d.keys())

    for x in list_k:
        new_d[x] *= 2

    return (new_d)
