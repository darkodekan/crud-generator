import csv
import random




customer_list = []

class Customer:
    def __init__(self, id, name_pers, ages_all, hobby, heh):
        
        self.id = id
        self.name_pers = name_pers
        self.ages_all = ages_all
        self.hobby = hobby
        self.heh = heh
    def __str__(self):
        return f"{ self.id }{ self.name_pers }{ self.ages_all }{ self.hobby }{ self.heh } "


def read():
    with open("Customer.csv", "w+") as f:
        citac = csv.reader(f)
        for row in citac:
            id = int(row[0])
            name_pers = row[1]
            ages_all = int(row[2])
            hobby = bool(row[3])
            heh = bool(row[4])
            customer_object = Customer(id,   name_pers,   ages_all,   hobby,   heh  )
            customer_list.append(customer_object)


def write():
    with open("Customer.csv", "w+") as f:
        writer = csv.writer(f)
        for customer_object in customer_list:
            writer.writerow([
                customer_object.id,
                customer_object.name_pers,
                customer_object.ages_all,
                customer_object.hobby,
                customer_object.heh,
                
                ])


def find_all():
    return customer_list


def find_by_id(id):
    for customer_object in customer_list:
        if customer_object.id == id:
            return customer_object
    return ValueError("no such element with that id")


def find(id=None, name_pers=None, ages_all=None, hobby=None, heh=None):
    filtered_list = customer_list
     
    if id is not None:
        filtered_list = [customer_object for customer_object in customer_list if customer_object.id == id] 
    if name_pers is not None:
        filtered_list = [customer_object for customer_object in customer_list if customer_object.name_pers == name_pers] 
    if ages_all is not None:
        filtered_list = [customer_object for customer_object in customer_list if customer_object.ages_all == ages_all] 
    if hobby is not None:
        filtered_list = [customer_object for customer_object in customer_list if customer_object.hobby == hobby] 
    if heh is not None:
        filtered_list = [customer_object for customer_object in customer_list if customer_object.heh == heh]
    return filtered_list


def save(customer_object):
    customer_list.append(customer_object)
    write()


def remove(id):
    index = __get_index(id)
    del customer_list[index]
    write()


def __get_index(id):
    for i, customer_object in enumerate(customer_list):
        if customer_object.id == id:
            return i
    raise ValueError("No such element")


def update(customer_object):
    index = __get_index(customer_object.id)
    customer_list[index] = customer_object
    write()


read()