#!/usr/bin/python3

"""
Summary: This module contains a function that demonstrates writing to
files in python
Author: Alemi Herbert Asiki <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""


def write_file(filename="", text=""):
    """
    This function writes a piece of text to a file
    It does not manage file permission exceptions
    It creates a file if it does not exist
    It overwrites the content of the file if it already exists

    Args:
        filename (string): the name of the file
        text (string): the text to be written to the file
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)