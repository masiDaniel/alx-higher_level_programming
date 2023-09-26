#!/usr/bin/python3
"""definition of a class square"""


class Square:
    """"representation of a square"""

    def __init__(self, size=0):
        """initialization of a new square

        Args:
            size(int): size of new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """gives the area of the square"""
        return (self.__size * self.__size)
