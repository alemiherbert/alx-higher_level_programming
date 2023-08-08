#!/usr/bin/python3
def uppercase(str):
    for char in str:
        c = ord(char)
        if c >= 97 and c <= 122:
            print("{}".format(chr(c - 32)), end='')
        else:
            print("{}".format(char), end='')
