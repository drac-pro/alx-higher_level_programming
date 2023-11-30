#!/usr/bin/python3
from sys import argv
num = len(argv)
if num == 1:
    print("0 arguments.")
else:
    print("{} argument{}:".format(num - 1, 's' if num > 2 else ''))
    for i in range(1, num):
        print("{}: {}".format(i, argv[i]))
