#!/usr/bin/python3
"""Defines write_file function"""


def write_file(filename="", text=""):
    """writes some text to a file
    Args:
        filename (file): the file
        text (str): the text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
