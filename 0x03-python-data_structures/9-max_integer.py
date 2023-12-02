#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_ = my_list[0]
    for i in my_list:
        max_ = i if i > max_ else max_
    return max_
