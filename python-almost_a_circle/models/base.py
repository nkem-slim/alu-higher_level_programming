#!/usr/bin/python3
""" This module contains a base class, which will later on become a subclass of another class
"""

import json
import os
import turtle
import tkinter


class Base:
    """ Manages 'id' attribute in all future classes to avoid code duplication

    Attributes:
        __nb_objects(int): Total number of objects created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization.
        Args:
            id (int): id of the class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries

        Args:
            list_dictionaries(:obj:`list` of `dict`): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            data_list = cls.from_json_string(file.read())
        return [cls.create(**data) for data in data_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes JSON string representation of list_objs to csv file"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                csv_form = "\n".join(
                    ",".join(str(value) for value in obj.values()) for obj in list_dict
                )
                f.write(csv_form)

    @classmethod
    def load_from_file_csv(cls):
        """Loads JSON from file"""
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            data_list = [line.strip().split(",") for line in file.readlines()]
        
        csv_headers = {
            "Rectangle": ["id", "width", "height", "x", "y"],
            "Square": ["id", "size", "x", "y"]
        }
        
        instance_list = []
        for data in data_list:
            dict_ = {key: int(value) for key, value in zip(csv_headers[cls.__name__], data)}
            instance_list.append(cls.create(**dict_))
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws a rectangle or a square using the turtle module."""
        line = turtle.Turtle()
        line.speed(1)
        
        for rectangle in list_rectangles:
            line.penup()
            line.goto(rectangle.x, rectangle.y)
            line.pendown()
            for _ in range(2):
                line.forward(rectangle.width)
                line.right(90)
                line.forward(rectangle.height)
                line.right(90)
        
        for square in list_squares:
            line.penup()
            line.goto(square.x, square.y)
            line.pendown()
            for _ in range(4):
                line.forward(square.size)
                line.right(90)
        
        turtle.done()
