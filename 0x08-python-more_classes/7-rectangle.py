#!/usr/bin/python3
""" rectangle class"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instantiation of width,  height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ gettter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ string representation of rectangle by using #"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """string representation of rectangle object"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ prints message when object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
