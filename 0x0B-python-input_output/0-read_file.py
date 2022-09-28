#!/usr/bin/python3
"""
Module-0
Contains function reads a text file and prints it to stdout
"""


def read_file(filename=''):
    """Read and print text from file"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
