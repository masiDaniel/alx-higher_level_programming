#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_mat = matrix.copy()

    for a in range(len(matrix)):
        n_mat[a] = list(map(lambda x: x**2, matrix[a]))

    return (n_mat)
