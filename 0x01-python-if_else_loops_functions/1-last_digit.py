#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int((abs(number) % 10) * (number / abs(number)))
print("Last digit of {} is {} and is ".format(number, last_digit), end = "")
if last_digit > 5:
    print("greater than 5")
elif (last_digit < 6 and last_digit != 0):
    print("less than 6 and not 0")
else:
    print("0")
