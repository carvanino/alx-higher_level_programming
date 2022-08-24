#!/usr/bin/python3
def remove_char_at1(str, n):
    i = 0
    for a in str:
        if i == n:
            a = ""
        i = i + 1
        print(a, end="")
    return ''
    #print()
