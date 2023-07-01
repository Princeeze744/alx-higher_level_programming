#!/usr/bin/python3
"""2-matrix_divided module"""


def matrix_divided(matrix, div):
    """Function divides each element in matrix by div

    Args:
        matrix: list of lists of integers/floats
        div(int/float): Denominator

    Return: matrix of floats rounded to 2d.p
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for index, row in enumerate(matrix):
        new_row = []
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        for i, elem in enumerate(row):
            if i > 0 and len(matrix[index]) != len(matrix[index-1]):
                raise TypeError("Each row of the matrix must have\
 the same size")
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            new_row.append(round((elem / div), 2))
        new_matrix.append(new_row)
    return new_matrix
