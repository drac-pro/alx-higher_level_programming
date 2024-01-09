#!/usr/bin/python3
"""Defines class_to_json function"""


def class_to_json(obj):
    """eturns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    Args:
        obj (object): data structure object
    """
    return obj.__dict__
