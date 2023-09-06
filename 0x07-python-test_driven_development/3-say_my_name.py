#!/usr/bin/python3

"""
this module contains self-introduction functions
"""


def say_my_name(first_name, last_name=""):
    """A funtion that introduces you

    Args:
        first_name (string): your first name
        last_name (string): your last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
