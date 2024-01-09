#!/usr/bin/python3
"""Defines append_write function"""


def append_write(filename="", text=""):
    """appends some text to a file
    Args:
        filename (file): the file
        text (str): the text
    Returns:
        int: number of characters writing
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
