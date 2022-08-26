#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arg = len(sys.argv)
    argv = sys.argv
    if arg != 4:
        print("Usage: {} <a> <operator> <b>" .format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator == "+":
        result = add(a, b)
        print("{} {} {} = {}" .format(argv[1], argv[2], argv[3], result))
    elif operator == "-":
        result = sub(a, b)
        print("{} {} {} = {}" .format(argv[1], argv[2], argv[3], result))
    elif operator == "*":
        result = mul(a, b)
        print("{} {} {} = {}" .format(argv[1], argv[2], argv[3], result))
    elif operator == "/":
        result = div(a, b)
        print("{} {} {} = {}" .format(argv[1], argv[2], argv[3], result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
