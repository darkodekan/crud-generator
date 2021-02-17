import csv
import random

person_list = []

class person:
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
    def __str__(self):
        return f"{ self.name }{ self.age } "

def read():
    with open("person.csv", "w+") as f:
        citac = csv.reader(f)
        for row in citac:
            name = row[0]
            age = int(row[1])
            person_object = person(name,   age  )
            person_list.append(person_object)

def write():
    with open("person.csv", "w+") as f:
        writer = csv.writer(f)
        for person_object in person_list:
            writer.writerow([
                person_object.name,
                person_object.age,
                
                ])
def find_all():
    return person_list

def find_by_id(id):
    for person_object in person_list:
        if person_object.id == id:
            return person_object
    return ValueError("no such element with that id")

def find(name=None, age=None):
    filtered_list = person_list
     
    if name is not None:
        filtered_list = [person for person in person_list if person.name == name] 
    if age is not None:
        filtered_list = [person for person in person_list if person.age == age]
    return filtered_list


def save(person_object):
    person_list.append(person_object)
    write()


def remove(id):
    index = __get_index(id)
    del person_list[index]

    write()

def __get_index(id):
    for i, person_object in enumerate(person_list):
        if person_object.id == id:
            return i
    raise ValueError("No such element")


def update(person_object):
    index = __get_index(person_object.id)
    person_list[index] = person_object
    write()

read()