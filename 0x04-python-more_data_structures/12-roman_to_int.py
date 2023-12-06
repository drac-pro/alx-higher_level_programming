#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for i in range(len(roman_string)):
        current = my_dict[roman_string[i]]
        new = my_dict[roman_string[i + 1]] if i < len(roman_string) - 1 else 0
        if current < new:
            value -= current
        else:
            value += current
    return int(value)
