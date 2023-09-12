#!/usr/bin/python3


"""
Summary: A module that demonstrates file reading
Author: Alemi Herbert Asiki <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert Asiki 2023
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF) and prints it to stdout
    Args:
        filename (string): the filename
    """

    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())
