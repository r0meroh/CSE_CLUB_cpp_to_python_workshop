from person import *
from worker import *
import functions as fun

def main():

    # create list of both types of objects

    people = []
    workers = []

    # prompt user
    answer = input("adding a Person, worker? Or type exit to stop\n")
    answer = answer.upper()

    while answer != 'EXIT':


        # if anwer is person, create a person object and append it to list
        if answer == 'PERSON':
            name = input('Enter name of person:\n')
            age = input('Enter age of person:\n')

            name = person(name, age)
            people.append(name)
            print('the following person was added:' )
            fun.display_person(name)

        elif answer == 'WORKER':
            name = input('Enter name of worker\n:')
            age = input('Enter age of worker: \n')
            occupation = input('Enter occupation of worker: ')


            name = worker(name,age,occupation)
            workers.append(name)
            print('the following worker was added: ')
            fun.display_worker(name)
        else:
            print('invalid choice, please try again...\n')

        answer = input("adding a Person, worker? Or type exit to stop\n")
        answer = answer.upper()


    # outside of loop
    return people, workers

def print_lists(list):
    for item in list:
        print(item)


if __name__ == '__main__':

    list_of_people, list_of_workers = main()

    print('The following people were added:')
    print_lists(list_of_people)

    print('The following workers were added: ')
    print_lists(list_of_workers)
