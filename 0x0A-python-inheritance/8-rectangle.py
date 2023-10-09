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
