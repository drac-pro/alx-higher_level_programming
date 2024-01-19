#!/usr/bin/python3
"""Defines a class Base"""
import json
import csv
import turtle
import os


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
            return "[]"
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
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv
        Args:
            list_objs (list): list of objects
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes from csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                list_dicts = [{k: int(v) for k, v in d.items()}
                        for d in reader]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list): list of rectangle objects
            list_squares (list): list of square objects
        """
        """os.environ['DISPLAY'] = ':0'"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#0e042b")
        turt.pensize(4)
        turt.shape("turtle")

        turt.color("#5c8504")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#1b9e93")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()
        turtle.exitonclick()
