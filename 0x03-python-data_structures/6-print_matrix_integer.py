#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in matrix[i]:
            print("{}{}".format(j, ' ' if j != matrix[i][-1] else ''), end='')
        print()
