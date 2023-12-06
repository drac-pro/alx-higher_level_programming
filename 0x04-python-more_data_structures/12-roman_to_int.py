#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for char in roman_string:
        if my_dict[char] > value:
            value = my_dict[char] - value
        else:
            value += my_dict[char]
    return value
