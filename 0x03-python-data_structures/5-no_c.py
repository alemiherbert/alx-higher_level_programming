#!/usr/bin/python3

def no_c(my_string):
    new_string = ""

    for character in my_string:
        if not character in "Cc":
            new_string += character

    return new_string
