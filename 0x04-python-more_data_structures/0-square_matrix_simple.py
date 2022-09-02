#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Compute square value of all integers of matrix
    """
    return ([[(x**2) for x in row] for row in matrix])
