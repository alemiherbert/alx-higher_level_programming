#!/usr/bin/python3

"""
Summary: This module contains a function that demonstrates appending textto files in python
Author: Alemi Herbert Asiki <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""


def append_write(filename="", text=""):
    """
    This function appends a piece of text to a file
    It does not manage file permission or existence exceptions
    It creates a file if it does not exist

    Args:
        filename (string): the name of the file
        text (string): the text to be written to the file
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
