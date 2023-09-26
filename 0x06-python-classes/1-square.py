#!/usr/bin/python3
"""defining a class called square"""


class Square:
    """ representation of the square class"""

    def __init__(self, size=0):
        """a new square

        Args:
            size (int): Size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
