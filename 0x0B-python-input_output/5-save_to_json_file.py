#!/usr/bin/python3

"""
Summary: This file contains functions that write an object to a text
file using JSON representation
Author: Alemi Herber Asiki <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file, using JSOn representation
    File permission exceptions are not handled
    Unserialisable objects exceptions are not handled
    Args:
        my_obj (any): the object
        filename (string): the filename
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
