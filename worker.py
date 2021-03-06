# worker class
# include person class from person.py

from person import *

class worker(person):

    # default constructor
    def __init__(self):
        name = ""
        age = 0
        occupation = ""

    # constructor with parameters
    def __init__(self,name, age, occupation):
        super().__init__(name,age)
        self.occupation = occupation

    # accessors
    def get_occupation(self):
        return self.occupation

    # mutators
    def set_occupation(occupation):
        self.occupation = occupation

    def __str__(self):
        return '{} {} {}'.format(self.name, self.age, self.occupation)
