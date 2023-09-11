#!/usr/bin/python3


"""
Contains functions that checks if an object directly or indirectly
inherited from the specified class
"""

def inherits_from(obj, a_class):
    """Checks if an object is only a subclass"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)