#!/usr/bin/python3
"""lazy_matrix_mul"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrix using numpy
    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    Returns:
        list: matrix product
    """
    return (np.matmul(m_a, m_b))
