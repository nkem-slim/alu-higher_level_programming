#!/usr/bin/python3
""" Create json from a file """
import json


def load_from_json_file(filename):
    """ deserialises from a file """
    with open(filename, mode="r", encoding="utf-8") as f:
        x = json.load(f)
    return x
