#!/usr/bin/python3

"""
This module contains a function that adds 2 integers
"""

def add_integer(a, b=98):
    """
    This function adds 2 integers
    Floats are casted into ints before the arithmetic

    Raises:
        TypeError: if either a or b is not an integer or float
    """
    if not type(a) is int and not type(a) is float:
        raise TypeError("a must be an integer")
    if not type(b) is int and not type(b) is float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)