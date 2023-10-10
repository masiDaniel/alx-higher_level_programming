#!/usr/bin/python3
""" json"""
import json


def to_json_string(my_obj):
    """ retuns json representation of an object
    Args:
        my_obj: the object that will be onverted to json
    """

    return json.dumps(my_obj)
