#!/usr/bin/python3
"""matrix multiplicatinon"""


def matrix_mul(m_a, m_b):
    """multiplies a ixn matrix by an nxj matrix
    Args:
        m_a(list): matrix 1
        m_b(list): matrix 2

    returns:
        list: matrix product
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    row1 = len(m_a)
    if row1 == 0 or not all(m_a):
        raise ValueError("m_a can't be empty")
    row2 = len(m_b)
    if row2 == 0 or not all(m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")
    col1 = len(m_a[0])
    if not all(len(row) == col1 for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    col2 = len(m_b[0])
    if not all(len(row) == col2 for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if col1 != row2:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[] for _ in range(row1)]
    for i in range(row1):
        for j in range(col2):
            ans = 0
            for z in range(row2):
                ans += m_a[i][z] * m_b[z][j]
            result[i].append(ans)
    return (result)
