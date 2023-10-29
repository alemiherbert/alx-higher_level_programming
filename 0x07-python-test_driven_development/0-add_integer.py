#!/usr/bin/python3

"""
add_integer.py - this module contains a function that adds two integers
"""


def add_integer(a, b=98):
    """This function adds two integers"""
    if not type(a) is int and not type(a) is float:
        raise TypeError("a must be an integer")
    if not type(b) is int and not type(b) is float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
