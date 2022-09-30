#!usr/bin/python3
"""Base Module
Houses a Base class with private attributes
"""


class Base:
    """ Defines the class Base
    """
    
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """ Initializes an Instance of class

        Args:
            id: (int) Defaults as None
        
        """

        if id != None:
            self.id = id
        Base.__nb_objects += 1