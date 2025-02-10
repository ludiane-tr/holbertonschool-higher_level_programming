#!/usr/bin/python3
'''Function that writes a string to a text file'''


def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
        return len(text)
