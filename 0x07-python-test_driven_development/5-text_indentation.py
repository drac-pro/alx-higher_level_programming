#!/usr/bin/python3
"""5-text_indentation module"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? \
    and :
    Args:
        text (str): the text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    c = 0
    while c < len(text):
        if text[c] in ".?:":
            print(text[c])
            print()

            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
        elif text[c] == '\n':
            print()
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
        else:
            print(text[c], end='')
            c += 1
