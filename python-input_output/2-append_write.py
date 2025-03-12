#!/usr/bin/python3
""" Contains one function """


def append_write(filename="", text=""):
    """ Appends to a file """
    with open(filename, mode="a", encoding="utf-8") as f:
        nb = f.write(text)
    return nb
