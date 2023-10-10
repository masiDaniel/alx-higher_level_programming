#!/usr/bin/python3
""" function to append to a file"""


def append_write(filename="", text=""):
    """ appends text to file"""

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
