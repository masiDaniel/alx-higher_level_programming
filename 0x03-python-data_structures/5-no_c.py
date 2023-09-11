#!/usr/bin/python3

def no_c(my_string):
    """remove c and C"""
    copied = [x for x in my_string if x != 'C' and x != 'c']
    return ("" .join(copied))
