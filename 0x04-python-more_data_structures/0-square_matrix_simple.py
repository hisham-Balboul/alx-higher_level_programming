#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtrx = matrix.copy()
    for i in range(len(matrix)):
        mtrx = list(map(lambda x: x**2, matrix[i]))
    return (mtrx)
