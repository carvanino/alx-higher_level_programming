#!/usr/bin/python3
""" 100-appned_after Module
Defines a functio append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file after each line
    containing a specific string

    Args:
        filename: File to append after
        search_string: string to find in filename
        new_string: string to replace search string with

    """

    with open(filename, mode='r') as f:
        read_line = f.readlines()

    with open(filename, mode='w') as f_w:
        s = ""
        for line in read_line:
            if search_string in line:
                s = s + new_string

        f_w.write(s)
