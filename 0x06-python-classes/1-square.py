#!/usr/bin/python3
class Square:
    """Defines a Square of type <class>
    Private instance attribute: size
    Instantiation with size (no type/value verificatio)
    """
    def __init__(self, size):
        """ Initializing class privately """
        self.__size = size
