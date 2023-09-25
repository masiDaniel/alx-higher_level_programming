#!/usr/bin/python3

def magic_calculation(a, b):
    """magic calculator"""
    ans = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            else:
                ans += a ** b / x
        except:
            ans = b + a
            break
    return (ans)
