#!/usr/bin/python3
""" Size validation"""


class Square:
    """ Defines a class 'Square' """
    def __init__(self, size=0):
        """ Initializes class square and raise exceptions
        when size is not an int or is negative
        Args:
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Gets the area of the square"""
        return self.__size ** 2
