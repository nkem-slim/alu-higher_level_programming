#!usr/bin/python3
"""

Contains one module

"""


def text_indentation(text):
    """
    Prints a text with two new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    i = 0
    length = len(text)

    while i < length:
        print(text[i], end="")
        if text[i] in delimiters:
            print("\n")
            # Skip any spaces after the delimiter
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
