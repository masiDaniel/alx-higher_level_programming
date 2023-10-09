#!/usr/bin/python3
""" module containg Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inheritig from Rectangle class"""

    def __init__(self, size):
        """ instantiation of size"""

        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def area(self):
        """  the area"""
        return self.__size ** 2

    def __str__(self):
        """ string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
