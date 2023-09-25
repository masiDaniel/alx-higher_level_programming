#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """safely execute a function"""
    try:
        ans = fct(*args)
        return (ans)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
