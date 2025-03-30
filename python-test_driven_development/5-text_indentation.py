#!/usr/bin/python3
"""
Contains one module
"""

def text_indentation(text):
    """
    Prints a text with two new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    delimiters = {'.', '?', ':'}
    output = ""
    i = 0
    while i < len(text):
        output += text[i]
        if text[i] in delimiters:
            output += "\n\n"
            # Skip all spaces after punctuation
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    print(output.strip())
