#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """the Rectangle class"""
    no_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instances of width and height"""
        self.width = width
        self.height = height
        Rectangle.no_of_instances += 1

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) is not int:
            raise TypeError("width must be a integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) is not int:
            raise TypeError("height must be a integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return area"""
        return self.height * self.width

    def perimeter(self):
        """return perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """representation using #"""
        if self.height == 0 or self.width == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """representation of recangle object"""
        return "Rectamgle({}, {})".format(self.width, self.height)

    def __del__(self):
        """message when object is deleted"""
        print("Bye Rectangle...")
        Rectangle.no_of_instances -= 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """the biggest rectangle is returned"""
        if not isinstance(rect_1,  Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2,  Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """new Rectangle  instance"""
        return cls(size, size)