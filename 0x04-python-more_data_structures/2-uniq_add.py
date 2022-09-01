#!/usr/bin/python3
def uniq_add(my_list=[]):
    simple_list = set(my_list)
    sum = 0
    for a in simple_list:
        sum = sum + a
    return sum
