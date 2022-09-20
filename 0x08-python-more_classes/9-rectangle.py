#!/usr/bin/python3
""" Module 1-rectangle

Defines a simple rectangle with attribute

"""


class Rectangle:
    """ Defines the Rectangle class

    Variable:
        number_of_instance: (int) Defaults to 0
        Get instances
        print_symbol: Defaults to '#'
        Symbol for string representation

    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Returns an informal and nicely printable string
        representation of a Rectangle instance, with the character '#'
        """
        r_str = ''
        if self.__width == 0 or self.__height == 0:
            return ''
        for length in range(self.__height):
            for breadth in range(self.__width):
                r_str = r_str + str(self.print_symbol)
            r_str += '\n'
        return r_str[:-1]

    def __repr__(self):
        """ Returns an official string representation of a Rectangle instance
        that can create an new instance of Rectangle by using eval()"""
        return ("Rectangle({}, {})" .format(self.__width, self.__height))

    def __del__(self):
        """ Detects deletion of an instance and display a prompt -
        'Bye rectangle' """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """ Obtains the Area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the Perimeter of rectangle
        or 0 if either with or height equals 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area

        Args:
            rect_1
            rect_2
        Raises:
            TypeError: rect_1/rect_2 must be an instance of Rectangle

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance

        Args:
            size: size/length of the rectangle

        """
        return cls(size, size)
