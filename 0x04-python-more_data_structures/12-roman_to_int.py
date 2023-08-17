#!/usr/bin/python3

def roman_to_int(roman_string):
    
    if roman_string == None:
        return 0
    if not isinstance(roman_string, str):
        return 0

    numeral_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    roman_string.upper()
    for i in range(len(roman_string)):
        result += numeral_map[roman_string[i]]
    return result

