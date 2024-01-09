#!/usr/bin/python3
"""Defines append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a specific
    string
    Args:
        filename (str): file
        search_string (str): string to be searched
        new_string (str): new string to be writing
    """
    content = ""
    with open(filename) as f:
        for line in f:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, 'w') as new_f:
        new_f.write(content)
