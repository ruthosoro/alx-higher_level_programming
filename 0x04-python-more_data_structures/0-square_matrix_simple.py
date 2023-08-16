#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    squared_matrix = list(map(lambda row: list(map(lambda x: x * x, row)),
                              matrix))
    return squared_matrix
