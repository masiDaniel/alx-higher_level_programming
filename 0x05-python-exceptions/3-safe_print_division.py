#!/usr/bin/python3

def safe_print_division(a, b):
    """answer for division of a by b"""
    try:
        ans = a / b
    except (ZeroDivisionError, TypeError):
        ans = None
    finally:
        print("inside result: {}".format(ans))
    return (ans)
