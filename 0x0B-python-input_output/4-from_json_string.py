#!/usr/bin/python3
""" json"""
import json


def from_json_string(my_str):
    """ returns an object represented by a json string
    Args:
        my_str (str): the json string to be converted to an objet
    """
    return json.loads(my_str)
