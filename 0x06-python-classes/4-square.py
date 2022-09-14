#!/usr/bin/python3
""" Access and update private attribute"""


class Square:
    """ Defines a class 'Square' """
    def __init__(self, size=0):
        """ Initializes class square and raise exceptions
        when size is not an int or is negative
        Args:
            size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """ Retrieves the private attribute (size)"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size/property of the class to value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Gets the area of the square"""
        return self.__size ** 2
