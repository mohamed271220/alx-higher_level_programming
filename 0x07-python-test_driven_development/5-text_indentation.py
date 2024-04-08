#!/usr/bin/python3
""" Module that prints a text with 2
new lines after each of these characters: ., ? and : """

def text_indentation(text):
    """ Function that prints a text with 2
    new lines after each of these characters: ., ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
