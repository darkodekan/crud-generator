import csv
import random

product_list = []

class product:
    def __init__(self, name, price):
        
        self.name = name
        self.price = price
    def __str__(self):
        return f"{ self.name }{ self.price } "

def read():
    with open("product.csv", "w+") as f:
        citac = csv.reader(f)
        for row in citac:
            name = row[0]
            price = float(row[1])
            product_object = product(name,   price  )
            product_list.append(product_object)

def write():
    with open("product.csv", "w+") as f:
        writer = csv.writer(f)
        for product_object in product_list:
            writer.writerow([
                product_object.name,
                product_object.price,
                
                ])
def find_all():
    return product_list

def find_by_id(id):
    for product_object in product_list:
        if product_object.id == id:
            return product_object
    return ValueError("no such element with that id")

def find(name=None, price=None):
    filtered_list = product_list
     
    if name is not None:
        filtered_list = [product for product in product_list if product.name == name] 
    if price is not None:
        filtered_list = [product for product in product_list if product.price == price]
    return filtered_list


def save(product_object):
    product_list.append(product_object)
    write()


def remove(id):
    index = __get_index(id)
    del product_list[index]

    write()

def __get_index(id):
    for i, product_object in enumerate(product_list):
        if product_object.id == id:
            return i
    raise ValueError("No such element")


def update(product_object):
    index = __get_index(product_object.id)
    product_list[index] = product_object
    write()

read()