#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items())
    
    # sorted_dict is a list of tuples.
    for key, value in sorted_dict:
        print("{0}: {1}".format(key, value))
