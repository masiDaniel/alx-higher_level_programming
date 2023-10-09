#!/usr/bin/python3
"""module containing rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inheriting from BaseGeometry class"""

    def __init__(self, width, height):
        """instantiate height and width"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """gets the area"""

        return self.__width * self.__height

    def __str__(self):
        """string rep"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
