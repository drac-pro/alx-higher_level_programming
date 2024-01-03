#!/usr/bin/python3
"""0-add_integer module"""


def matrix_divided(matrix, div):
    """divides each number in a matrix by div
    Args:
        matrix (list): the matrix
        div (int/float): the denominator
    Returns:
        list: a new list with the results
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or not all(isinstance(row
        , list) for row in matrix) or not all(isinstance(x, (int, float)) for 
            row in matrix for x in row)):
        raise TypeError(msg)
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return list(map(lambda row: 
                list(map(lambda x: round(x/div, 2), row)), matrix))
