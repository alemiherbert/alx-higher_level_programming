#!/usr/bin/python3


"""
Summary: This script adds all arguments to a python list and saves
them to a file
Author: Alemi Herbert Asiki <alemiherbert@gmail.com>
Created: September 2023
(c) Alemi Herbert 2023
"""


import sys

if __name__ = "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        my_list = load_from_json_file("add_items.json")
    except FileNotFoundError:
        my_list = []
    my_list.extend[1:]
    save_to_json_file(items, "add_items.json")
