#!/usr/bin/python3
"""Defines read_file function"""


def read_file(filename=""):
    """reads and print the contents of a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
