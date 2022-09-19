#!/usr/bin/python3
""" Module 1-rectangle

Defines a simple rectangle with attribute

"""


class Rectangle:
    """ Defines the Rectangle class """

    def __init__(self, width=0, height=0):
        """
        Initialize class

        Args:
            width: (int) Defaults to 0
            height: (int) Defaults to 0

        Raises:
            TypeError: width or height must be an integer
            TypeError: width or height must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves private attribute (width) """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the class to value """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Retrieves private attribute (height) """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the class to value """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
