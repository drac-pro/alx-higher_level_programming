#!/usr/bin/python3
def print_last_digit(number):
    print("{}".format(abs(number) % ), end='')
    return (abs(number) % 10)
