#!/usr/bin/python3
""" rectangle Module
Houses a subclass Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Defines the Rectangle subclass
    """

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the private attribute (width)"""
        return self.__width
    @width.setter
    def width(self, value):
        """Set the width of the class to value """
        self.__width = value

    @property
    def height(self):
        """Retrives the private attribute (height) """
        return self.__height
    @height.setter
    def height(self, value):
        """Sets the (height) as a private attribute """
        self.__height = value
    
    @property
    def x(self):
        """ Retrieves the private attribute (x) """
        return self.__x
    @x.setter
    def x(self, value):
        """Sets (x) as a private attribute """
        self.__x = value
    
    @property
    def y(self):
        """ Retrieves the private attribute (y) """
        return self.__y
    def y(self, value):
        """Sets (y) as a private attribute """
        self.__y = value
