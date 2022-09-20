#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def unsigned(num): 
    return num if num >= 0 else num * -1


def get_l(num):
    return num % 10 if num >= 0 else (unsigned(num) % 10) * -1


l_digit = get_l(number)


def prnt(msg):
    print("Last digit of", number, "is", l_digit, msg, end="")


if l_digit > 5:
    prnt("and is greater than 5")
elif l_digit == 0:
    prnt("and is 0")
elif l_digit < 6 and l_digit != 0:
    prnt("and is less than 6 and not 0")
else:
    print("How did we get here?")
print()
