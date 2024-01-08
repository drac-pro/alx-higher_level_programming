#!/usr/bin/python3
"""Defines a class MyInt"""


class MyInt(int):
    """Represent a custom int class"""
    def __eq__(self, other):
        """Defines behavior for the equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Defines behavior for the inequality operator"""
        return super().__eq__(other)
