#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list):
        return 0
    numerator, denomenator = 0, 0
    for score in my_list:
        numerator += (score[0] * score[1])
        denomenator += score[1]
    return float(numerator)/denomenator
