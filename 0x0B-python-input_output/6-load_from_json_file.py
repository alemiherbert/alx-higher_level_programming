#!/usr/bin/python3

"""
Summary: This file contains a function that creates an object from a JSON file
Author: Alemi Herber Asiki <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""

import json


def load_from_json_file(filename):
    """
    This function creates an object from a json file
    File permission exceptions are not handled
    Strings that do not represent objects are not handled
    Args:
        filename (string): the filename
    """
    with open(filename, "r", encoding="utf-8") as file:
        return (json.load(file))
