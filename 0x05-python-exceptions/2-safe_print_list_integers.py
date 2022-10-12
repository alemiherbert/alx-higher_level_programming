#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    p = 0
    for item in my_list:
        try:
            if p < x:
                print("{:d}".format(item), end='')
                p += 1
        except (ValueError, TypeError):
            continue
        finally:
            print()
