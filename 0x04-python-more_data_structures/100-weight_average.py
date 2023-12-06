#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator, denomenator = 0, 0
    for score in my_list:
        numerator += (score[0] * score[1])
        denomenator += score[1]
    return float(numerator)/denomenator
