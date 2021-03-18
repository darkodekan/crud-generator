import csv
import random




item_list = []

class Item:
    def __init__(self, id, name, price, customer_id, asd):
        
        self.id = id
        self.name = name
        self.price = price
        self.customer_id = customer_id
        self.asd = asd
    def __str__(self):
        return f"{ self.id }{ self.name }{ self.price }{ self.customer_id }{ self.asd } "


def read():
    with open("Item.csv", "w+") as f:
        citac = csv.reader(f)
        for row in citac:
            id = int(row[0])
            name = row[1]
            price = float(row[2])
            customer_id = int(row[3])
            asd = row[4]
            item_object = Item(id,   name,   price,   customer_id,   asd  )
            item_list.append(item_object)


def write():
    with open("Item.csv", "w+") as f:
        writer = csv.writer(f)
        for item_object in item_list:
            writer.writerow([
                item_object.id,
                item_object.name,
                item_object.price,
                item_object.customer_id,
                item_object.asd,
                
                ])


def find_all():
    return item_list


def find_by_id(id):
    for item_object in item_list:
        if item_object.id == id:
            return item_object
    return ValueError("no such element with that id")


def find(id=None, name=None, price=None, customer_id=None, asd=None):
    filtered_list = item_list
     
    if id is not None:
        filtered_list = [item_object for item_object in item_list if item_object.id == id] 
    if name is not None:
        filtered_list = [item_object for item_object in item_list if item_object.name == name] 
    if price is not None:
        filtered_list = [item_object for item_object in item_list if item_object.price == price] 
    if customer_id is not None:
        filtered_list = [item_object for item_object in item_list if item_object.customer_id == customer_id] 
    if asd is not None:
        filtered_list = [item_object for item_object in item_list if item_object.asd == asd]
    return filtered_list


def save(item_object):
    item_list.append(item_object)
    write()


def remove(id):
    index = __get_index(id)
    del item_list[index]
    write()


def __get_index(id):
    for i, item_object in enumerate(item_list):
        if item_object.id == id:
            return i
    raise ValueError("No such element")


def update(item_object):
    index = __get_index(item_object.id)
    item_list[index] = item_object
    write()


read()