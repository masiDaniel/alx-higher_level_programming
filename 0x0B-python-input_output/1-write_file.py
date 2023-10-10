#!/usr/bin/python3
"""function to write to s file"""


def write_file(filename="", text=""):
    """the function itself"""

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
