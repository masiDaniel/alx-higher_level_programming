#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """multiples of 2"""
    muls = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            muls.append(True)
        else:
            muls.append(False)

    return (muls)
