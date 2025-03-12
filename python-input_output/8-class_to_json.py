#!/usr/bin/python3
""" Returns a dictionary description for a serialised object """


def class_to_json(obj):
    """ serialises object and returns a dictionary """
    return obj.__dict__
