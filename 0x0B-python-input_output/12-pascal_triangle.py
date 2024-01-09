#!/usr/bin/python3
"""Defines pascal_triangle function"""


def pascal_triangle(n):
    """"returns a list of lists of integers representing the Pascal’s
    triangle of n
    Args:
        n (int): the pascal triangle number
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                coef = 1
            else:
                coef = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(coef)
        triangle.append(row)
    return triangle
