#!/usr/bin/python3
"""
Contains one module
"""


def text_indentation(text):
    print(text.replace(". ", ".\n\n").replace("? ", "?\n\n").replace(": ", ":\n\n"))
