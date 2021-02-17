import csv
import random

Person_list = []

class Person:
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
    def __str__(self):
        return f"{ self.name }{ self.age } "

def read():
    with open("Person.csv", "w+") as f:
        citac = csv.reader(f)
        for row in citac:
            name = row[0]
            age = int(row[1])
            Person_object = Person(name,   age  )
            Person_list.append(Person_object)

def write():
    with open("Person.csv", "w+") as f:
        writer = csv.writer(f)
        for Person_object in Person_list:
            writer.writerow([
                Person_object.name,
                Person_object.age,
                
                ])
def find_all():
    return Person_list

def find_by_id(id):
    for Person_object in Person_list:
        if Person_object.id == id:
            return Person_object
    return ValueError("no such element with that id")

def find(name=None, age=None):
    filtered_list = Person_list
     
    if name is not None:
        filtered_list = [Person for Person in Person_list if Person.name == name] 
    if age is not None:
        filtered_list = [Person for Person in Person_list if Person.age == age]
    return filtered_list


def save(Person_object):
    Person_list.append(Person_object)
    write()


def remove(id):
    index = __get_index(id)
    del Person_list[index]

    write()

def __get_index(id):
    for i, Person_object in enumerate(Person_list):
        if Person_object.id == id:
            return i
    raise ValueError("No such element")


def update(Person_object):
    index = __get_index(Person_object.id)
    Person_list[index] = Person_object
    write()

read()