#!/usr/bin/python3

"""Module contains a class that inherits from the builtin list object"""

class MyList(list):
    """Implements sorted printing for the builtin list object"""

    def print_sorted(self):
        """Print a list in sorted ascending order"""
        print(sorted(self))
