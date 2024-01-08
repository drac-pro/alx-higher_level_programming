#!/usr/bin/python3
"""Defines a Mylist class"""


class MyList(list):
    """blueprint for Mylist object"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
