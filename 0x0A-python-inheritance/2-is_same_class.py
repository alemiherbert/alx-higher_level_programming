#!/usr/bin/python3

"""
This module defines a function that checks if an object
is an instance of a given class
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class
    Args:
        obj (any): the object
        a_class (type): the class to check

    Returns:
        True if an object is an instance of the class"""
    return (type(obj) == a_class)
