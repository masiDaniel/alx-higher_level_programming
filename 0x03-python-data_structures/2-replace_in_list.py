#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace element at specific position"""
    if idx < len(my_list) or idx >= 0:
        my_list[idx] = element
    return (my_list)
