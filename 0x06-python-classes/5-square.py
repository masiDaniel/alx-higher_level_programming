#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represention of a square."""

    def __init__(self, size):
        """Initialization of a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """current area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with # character."""
        for a in range(0, self.__size):
            [print("#", end="") for b in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
