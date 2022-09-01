#!/usr/bin/python3
def number_keys(a_dictionary):
    no_keys = 0
    if not a_dictionary:
        return
    for key, a in enumerate(a_dictionary):
        no_keys = no_keys + key
    return no_keys
