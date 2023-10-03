#!/usr/bin/python3
""" prints a square using #"""


def print_square(size):
    """prints a square using #
    
    Args:
        size(int): size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for a in range(size):
            print("#" * size)