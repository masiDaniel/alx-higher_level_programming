#!/usr/bin/python3
""" rectangle class"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """instantiation of width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ string representation of rectangle usinh #"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """string representation of rectangle object"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ prints message when object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
