#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for item in my_list:
            if i < x:
                print('{}'.format(my_list[i]), end='')
                printed += 1
        print()
    except TypeError:
        pass
    finally:
        return i
