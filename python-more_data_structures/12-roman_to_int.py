#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for c in reversed(roman_string):
        curr = values[c]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result
