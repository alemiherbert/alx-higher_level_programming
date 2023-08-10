#!/usr/bin/python3

def infinite_add(args):
    numbers = args[1:]
    sum = 0
    for number in numbers:
        sum += int(number)
    return sum


if __name__ == "__main__":
    from sys import argv
    print(infinite_add(argv))
