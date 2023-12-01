#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    length = len(argv)
    if length < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif length > 3 and argv[2] not in {'+', '-', '/', '*'}:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if operator == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif operator == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif operator == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif operator == '/':
            if b == 0:
                print("Division by zero is not allowed.")
            else:
                print("{:d} / {:d} = {:.2f}".format(a, b, div(a, b)))
                exit(1)
