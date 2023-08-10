#!/usr/bin/python3

import hidden_4
names = dir(hidden_4)
for name in names:
    if name.startswith("__"):
        print("{}".format(name))
