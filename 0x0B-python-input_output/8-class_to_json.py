#!/usr/bin/python3

"""
This function returns the dictionary description with simple data
structure
"""


def class_to_json(obj):
    """
    Return a dictionary representation of an object
    """
    return (obj.__dict__)
