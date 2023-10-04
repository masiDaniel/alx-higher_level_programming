#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """the Rectangle class"""
    def __init__(self, width=0, height=0):
        """instances of width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width """
        if type(value) is not int:
            raise TypeError("width must be a integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get width"""
        return self.__height

    @width.setter
    def height(self, value):
        """set the height"""
        if type(value) is not int:
            raise TypeError("height must be a integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value
