#!/usr/bin/python3
for a in range(ord('z'), ord('a') - 1, -2):
#for a in reversed(range(ord('b'), ord('z')+ 1, 2)):
    print("{:c}{:s}" .format(a, chr(a - 33)), end="")
