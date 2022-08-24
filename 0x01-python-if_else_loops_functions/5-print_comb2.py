#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if (a != 9 or b != 9):
            print("{:d}{:d}" .format(a, b), end=", ")
        else:
            print("{:d}{:d}" .format(a, b))
