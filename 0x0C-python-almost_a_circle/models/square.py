#!/usr/bin/python3
""" square Module
Houses a subclass Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines the subclass Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints an informal representation of an instance
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Retrieves the size of square
        """

        return self.width

    @size.setter
    def size(self, value):
        """ Sets the size of square to value
        """

        self.width = value
        self.height = value
