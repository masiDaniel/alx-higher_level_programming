#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """prints the first elements in a list

    Args:
        my_list(list): the list being printed from
        x(int): no of elements

    Returns:
        no of elements
    """
    num = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (num)
