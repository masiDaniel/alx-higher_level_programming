#!/usr/bin/python3

def magic_calculation(a, b):
    """bytecode provided by Holberton School"""
    from magic_calculation_102 import sub, add

    if a < b:
        d = add(a, b)
        for x in range(4, 6):
            d = add(d, x)
        return (c)

    else:
        return(sub(a, b))
