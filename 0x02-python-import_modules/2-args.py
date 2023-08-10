#!/usr/bin/python3

def print_args(args):
    number_of_args = len(args) - 1
    if (number_of_args == 0):
        print("0 arguments")
    if (number_of_args == 1):
        print("1 argument")
    else:
        print("{} arguments".format(number_of_args))
    for argument in range(number_of_args):
        print("{}: {}".format(argument + 1, args[argument + 1]))

if __name__ == "__main__":
    from sys import argv
    print_args(argv);
