#!/usr/bin/python3

"""
Contains functions that check" if an object somehow is
inherited anothers properties
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an inherited instance of a given class
    Args:
        obj (any): the object
        a_class (type): the class to check

    Returns:
        True if an object is an inherited instance of the class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
