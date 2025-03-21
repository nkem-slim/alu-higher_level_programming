#!/usr/bin/python3
""" Contains one function """
import json


def save_to_json_file(my_obj, filename):
    """ Serialises to a file """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
