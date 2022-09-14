#!/usr/bin/python3
""" Access and update private attribute"""


class Square:
    """ Defines a class 'Square' """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes class square and raise exceptions
        when size is not an int or is negative
        Args:
            size: size of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Retrieves the private attribute (position)"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position o fthe class to value """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Gets the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """ Prints a graphical representation of square size to stdout """
        # if self.__position[1] > 0:
        # print()
        if self.__size == 0:
            print()
            return ("")

        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()

    def __str__(self):
        """Defines the print representation of square"""
        if self.__size != 0:
            [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print()
        return ("")
