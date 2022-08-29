#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    if not my_list:
        return
    while idx >= 0:
        print("{:d}" .format(my_list[idx]))
        idx = idx - 1
