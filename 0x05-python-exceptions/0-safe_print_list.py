#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for item in range(x):
            print('{}'.format(my_list[item]), end='')
            printed += 1
        print()
    except TypeError, IndexError:
        pass
    finally:
        return printed
