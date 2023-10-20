#!/usr/bin/python3
"""rectangle class"""

from .base import Base


class Rectangle(Base):
    """rectangle class inheriting from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for 'width'
    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    # Getter and setter for 'height'
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value

    # Getter and setter for 'x'
    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    # Getter and setter for 'y'
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """return the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """ uses # to print out the rectangle"""
        for x in range(self.__y):
            print()
        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
    def update(self, *args, **kwargs):
        """attributes update"""
        if args:
            attrbutes = ["id", "width", "height", "x", "y"]
            for x, arg in enumerate(args):
                setattr(self, attrbutes[x], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self,key, value)

    def to_dictionary(self):
        """dictionary representstion of Rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}

    def __str__(self):
        """string repr"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
