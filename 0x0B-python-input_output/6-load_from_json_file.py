#!/usr/bin/python3
"""Defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    Args:
        filename (str): file name
    """
    with open(filename, encoding='utf-8') as f:
        json.load(f)
