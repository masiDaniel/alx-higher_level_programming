#!/usr/bin/python3
"""matrix division function"""


def matrix_divided(matrix, div):
    """divide elements of a matrix

    Args:
        matrix (list): a list of integers or floating point
        div (int/float): divisor
    Returns:
        a new matrix containing the results of the division
    """

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return ([list(map(lambda x: round(x / div, 2).row)) for row in matrix])
