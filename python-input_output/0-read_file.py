#!/usr/bin/python3
'''Function that reads a text file (UTF8) and prints it to stdout'''

def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as file:
        for words in file:
            print("{}".format(words), end="")
