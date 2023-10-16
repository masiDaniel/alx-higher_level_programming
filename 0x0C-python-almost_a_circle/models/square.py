#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    """class squre"""

    def __init__(self, size, x=0, y=0, id=None):
        """super instance"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""

        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updating of attributes"""

        if args:
            attributes = ["id", "size", "x", "y"]
            for x, arg in enumerate(args):
                setattr(self, attributes[x], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of the square"""

        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """string rep"""

        return "[square] ({}) {}/{} - {}" .format(self.id, self.x, self.y, self.width)
