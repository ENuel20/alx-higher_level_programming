#!/usr/bin/python3
"""
    module Base.py
    contains a class Base
    contains a public class attribue id
    and a private class attribute
"""

class Base:
    """
        defines a class Base
        Args:
            id(int): id
            __nb_objects(int):
        instances:
            __init__(self, id = None):
    """

    __nb_objects = 0

    def __init__(self, id = None):
        """ initializing the class"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects



