#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        # new_string = my_string.translate({ord(i): None for i in 'cC'})
        if i == "c" or i == "C":
            i = ''
        print("{}" .format(i), end='')
    return ''
    # new_string
