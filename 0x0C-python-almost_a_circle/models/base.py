#!/usr/bin/python3
"""Defines a class Base"""
import json


class Base:
    """Defines a base object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initiallizes a base Instance
        Args:
            id (int): id of new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list):  list of instances who inherits of Base
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jf.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string (str): string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            dictionary (dict): dictionary of attributes
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as json_file:
                list_dicts = Base.from_json_string(json_file.read())
            return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []
