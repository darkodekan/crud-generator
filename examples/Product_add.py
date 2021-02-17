import csv
import random

Product_list = []

class Product:
    def __init__(self, name, price):
        
        self.name = name
        self.price = price
    def __str__(self):
        return f"{ self.name }{ self.price } "

def read():
    with open("Product.csv", "w+") as f:
        citac = csv.reader(f)
        for row in citac:
            name = row[0]
            price = float(row[1])
            Product_object = Product(name,   price  )
            Product_list.append(Product_object)

def write():
    with open("Product.csv", "w+") as f:
        writer = csv.writer(f)
        for Product_object in Product_list:
            writer.writerow([
                Product_object.name,
                Product_object.price,
                
                ])
def find_all():
    return Product_list

def find_by_id(id):
    for Product_object in Product_list:
        if Product_object.id == id:
            return Product_object
    return ValueError("no such element with that id")

def find(name=None, price=None):
    filtered_list = Product_list
     
    if name is not None:
        filtered_list = [Product for Product in Product_list if Product.name == name] 
    if price is not None:
        filtered_list = [Product for Product in Product_list if Product.price == price]
    return filtered_list


def save(Product_object):
    Product_list.append(Product_object)
    write()


def remove(id):
    index = __get_index(id)
    del Product_list[index]

    write()

def __get_index(id):
    for i, Product_object in enumerate(Product_list):
        if Product_object.id == id:
            return i
    raise ValueError("No such element")


def update(Product_object):
    index = __get_index(Product_object.id)
    Product_list[index] = Product_object
    write()

read()