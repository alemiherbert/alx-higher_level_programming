#!/usr/bin/python3
import random
number = random.randint(-10000, 20000)

unsigned = lambda num: num if num >= 0 else num * -1
l_digit = unsigned(number) % 10
prnt = lambda msg: print("Last digit of", number, "is", l_digit, msg, end="")


if l_digit > 5:
    prnt("and is greater than 5")
elif l_digit == 0:
    prnt("and is 0")
elif l_digit < 6 and l_digit != 0:
    prnt("and is less than 6 and not 0")
else:
    print("How did we get here?")
print()
