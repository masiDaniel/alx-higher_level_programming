#!/usr/bin/python3
"""returns true if object is an istaince of
 aclass inherited from the specified class"""


def inherits_from(obj, a_class):
    """function"""

    return type(obj) != a_class and isinstance(obj, a_class)
