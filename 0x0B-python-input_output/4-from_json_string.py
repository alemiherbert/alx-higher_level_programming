#!/usr/bin/python3

"""
Summary: This module contains a function that returns a python object
represented by a JSON string
Author: Alemi Herbert Asiki <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""

import json


def from_json_string(my_str):
    """
    This function returns a python object represented by a JSON string
    It does not handle exceptions for JSON strings that do not represent
    an object

    Args:
        my_str (any): the object
    """
    return (json.loads(my_str))
