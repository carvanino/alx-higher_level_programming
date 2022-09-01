#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    square_matrix = []
    for a in range(len(matrix)):
        square_matrix.append(list(map(lambda x: x ** 2, matrix[a])))
    return (square_matrix)
