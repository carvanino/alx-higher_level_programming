#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a + 1, 10):
        if (a == b):
            continue
        elif(a != 8):
            print("{:d}{:d}" .format(a, b), end=", ")
        else:
            print("{:d}{:d}" .format(a, b))
