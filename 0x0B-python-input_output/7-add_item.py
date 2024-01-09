#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file.py').\
        load_from_json_file

    try:
        lst = load_from_json_file("add_item.json")
    except FileNotFoundError:
        lst = []
    lst.append(sys.argv[1:])
    save_to_json_file(lst, "add_item.json")
