from person import *
from worker import *

# functions
def display_person(person):
    print('Name: ')
    print(person.get_name())
    print('age: ')
    print( person.get_age())

def display_worker(worker):
    print('Name: ')
    print(worker.get_name())
    print('age: ')
    print(worker.get_age())
    print('occupation: ')
    print(worker.get_occupation())
