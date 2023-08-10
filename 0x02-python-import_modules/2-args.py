#!/usr/bin/python3

from sys import argv

number_of_args = len(argv) - 1

if (number_of_args == 0):
    print("0 arguments")
if (number_of_args == 1):
    print("1 argument")
else:
    print("{} arguments".format(number_of_args))
for argument in range(number_of_args):
    print("{}: {}".format(argument + 1, argv[argument + 1]))
