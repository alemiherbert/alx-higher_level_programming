#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    _printed = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            _printed += 1
    except IndexError:
        break
    print("")
    return (_printed)
