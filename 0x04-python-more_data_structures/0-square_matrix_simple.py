#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtrx = matrix.copy()
    for i in range(len(matrix)):
        mtrx[i] = list(map(lambda x: x**2, matrix[i]))
    return (mtrx)
