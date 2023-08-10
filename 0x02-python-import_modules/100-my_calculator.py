#!/usr/bin/python3

def calculate(a, op, b):
    if (op == '+'):
        return a + b
    if (op == '-'):
        return a - b
    if (op == '*'):
        return a * b
    if (op == '/'):
        return a / b
    return None


if __name__ == "__main__":
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    result = calculate(a, operator, b)
    if result is None:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))
