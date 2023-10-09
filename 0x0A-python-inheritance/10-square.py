#!/usr/bin/python3
"""module containing square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inheritin gfrom rectangle class"""

    def __init__(self, size):
        """intantattion of size"""
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """computes the area"""
        return self.__size ** 2
