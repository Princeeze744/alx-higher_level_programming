#!/usr/bin/python3
"""Find the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function finds list of integers"""
    if list_of_integers is not None and len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
