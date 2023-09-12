#!/usr/bin/python3

"""
Summary: This module contains a function that returns the JSON
representation of an object
Author: Alemi Herbert Asiki <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""

import json


def to_json_string(my_obj):
    """
    This function returns a JSON representation of a string
    It does not handle exceptions for non-serialisable objects

    Args:
        my_obj (any): the object
    """
    return (json.dumps(my_obj))
