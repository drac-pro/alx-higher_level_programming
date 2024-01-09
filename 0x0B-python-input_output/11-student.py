#!/usr/bin/python3
"""Defines class Student"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student object
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance"""
        if type(attrs) == list and all(type(ele) == str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Args:
            json (dict): a dictionary to replace atttributes with
        """
        for k, v in json.items():
            setattr(self, k, v)
