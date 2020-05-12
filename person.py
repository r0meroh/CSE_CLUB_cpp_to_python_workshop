# Hugo Romero
# 5/11/2020
# Cpp to python workshop

#person.py

"""
    In python vector, string, and iostream(input/output
    stream are native to the standard library)
"""

class person:
    # in python all class functions are public unless specified

    # default constructor
    def __init__(self):

        name = ""
        age = 0

    # constructor with parameters
    def __init__(self, name, age):

        self.name = name
        self.age = age

    # accessors

    # get name
    def get_name():
        return name

    # get age
    def get_age():
        return age

    #mutators

    #set set_name
    def set_name(name):
        self.name = name

    # set age
    def set_age(age):
        self.age = age

    def __str__(self):
        return '{} {}'.format(self.name, self.age)
