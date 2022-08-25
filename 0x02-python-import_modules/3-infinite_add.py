#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    arg = len(sys.argv)
    if arg == 1:
        print("{}" .format(arg - 1))
    elif arg > 1:
        i = 1
        sum = 0
        while i < arg:
            sum = sum + int(sys.argv[i])
            i = i + 1
        print("{}" .format(sum))
