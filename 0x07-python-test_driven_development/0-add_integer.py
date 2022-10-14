#!/usr/bin/python3
"""
The add_integer module contains a function that adds two integers.
"""


def add_integer(a:int, b:int=98):
    """
    This functon adds two integers
    """

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
