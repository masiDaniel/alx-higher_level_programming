#!/usr/bin/python3
"""json """
import json


def save_to_json_file(my_obj, filename):
    """writes  object to  text file using json representation
    Args:
        my_obj: object
        filename: text file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
