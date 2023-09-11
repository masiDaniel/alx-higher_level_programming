#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replace element without modifying list"""
    if idx > (len(my_list) - 1) or idx < 0:
        return (my_list)

    buf = [x for x in my_list]
    buf[idx] = element
    return (copy)
