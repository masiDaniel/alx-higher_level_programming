#!/usr/bin/python3
""" contains a function that finds the peak in a
list of unsorted integers"""


def find_peak(list_of_integers):
    """ the function"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
