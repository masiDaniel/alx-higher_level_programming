#!/usr/bin/python3
"""module documentation"""


def pascal_triangle(n):
    """ returns a list of integers representing the
    Pascal's triangle of n"""

    if n <= 0:
        return []

    p_triangle = [[1]]

    for x in range(1, n):
        prev_row = p_triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        p_triangle.append(new_row)

    return p_triangle
