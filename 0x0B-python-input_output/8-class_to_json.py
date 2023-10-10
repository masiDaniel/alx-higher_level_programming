#!/usr/bin/python3
"""class"""


def class_to_json(obj):
    """returns dictionary description with simple data
    structure for json serialization of an object"""

    return obj.__dict__
