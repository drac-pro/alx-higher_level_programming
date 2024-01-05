#!/usr/bin/python3
"""magic_string"""


def magic_string():
    """ Returns the string “BestSchool” n times base on an outside loop"""
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return "BestSchool, " * (magic_string.counter - 1) + "BestSchool"
