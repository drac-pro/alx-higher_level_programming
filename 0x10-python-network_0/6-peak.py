#!/usr/bin/python3
"""defines a function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers
    Args:
        list_of_integers(list): list of integers
    Returns:
        peak(int)
    """
    if list_of_integers == []:
        return None
    size = len(list_of_integers)
    if size == 1 or list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    for i in range(1, size - 1):
        if list_of_integers[i] >= list_of_integers[i-1] and\
                list_of_integers[i] >= list_of_integers[i+1]:
            return list_of_integers[i]
