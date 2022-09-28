#!/usr/bin/python3
import json
""" 3-to_json_string Module
Defines a function t0_json_string
"""


def to_json_string(my_obj):
    """ Retuns the JSON representation of an object(string)

    Args:
        my_obj: A python object

    Returns: a JSON representation of my_obj
    """

    return json.dumps(my_obj)
