#!/usr/bin/python3

def remove_char_at(_str, idx):
    copy = ""
    for i in range(len(_str)):
        if i != idx:
            copy += _str[i]
    return copy
