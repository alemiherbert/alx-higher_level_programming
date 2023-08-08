#!/usr/bin/python3
def uppercase(str):
    for char in str:
        c = ord(char)
        if c >= 97 and c <= 122:
            c -= 32
        print("{}".format(char), end='')
        print("{}".format(""))
