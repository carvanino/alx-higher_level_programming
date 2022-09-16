#!/usr/bin/python3
""" Module add-integer  
Adds two Integers/Floats """


def add_integer(a, b=98):
    """ Returns the sum of the addition of a and b
    or raise a TypeError is either a or b is not an
    integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
