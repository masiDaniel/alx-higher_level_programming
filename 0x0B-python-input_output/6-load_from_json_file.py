#!/usr/bin/python3
""" json"""
import json


def load_from_json_file(filename):
    """ create object from a json file
    Args:
        filename: json file
    """

    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
