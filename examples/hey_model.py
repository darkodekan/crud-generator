import csv
import random




hey_list = []

class Hey:
    def __init__(self, id, price, asd, uff):
        
        self.id = id
        self.price = price
        self.asd = asd
        self.uff = uff
    def __str__(self):
        return f"{ self.id }{ self.price }{ self.asd }{ self.uff } "


def read():
    with open("Hey.csv", "w+") as f:
        citac = csv.reader(f)
        for row in citac:
            id = int(row[0])
            price = float(row[1])
            asd = row[2]
            uff = row[3]
            hey_object = Hey(id,   price,   asd,   uff  )
            hey_list.append(hey_object)


def write():
    with open("Hey.csv", "w+") as f:
        writer = csv.writer(f)
        for hey_object in hey_list:
            writer.writerow([
                hey_object.id,
                hey_object.price,
                hey_object.asd,
                hey_object.uff,
                
                ])


def find_all():
    return hey_list


def find_by_id(id):
    for hey_object in hey_list:
        if hey_object.id == id:
            return hey_object
    return ValueError("no such element with that id")


def find(id=None, price=None, asd=None, uff=None):
    filtered_list = hey_list
     
    if id is not None:
        filtered_list = [hey_object for hey_object in hey_list if hey_object.id == id] 
    if price is not None:
        filtered_list = [hey_object for hey_object in hey_list if hey_object.price == price] 
    if asd is not None:
        filtered_list = [hey_object for hey_object in hey_list if hey_object.asd == asd] 
    if uff is not None:
        filtered_list = [hey_object for hey_object in hey_list if hey_object.uff == uff]
    return filtered_list


def save(hey_object):
    hey_list.append(hey_object)
    write()


def remove(id):
    index = __get_index(id)
    del hey_list[index]
    write()


def __get_index(id):
    for i, hey_object in enumerate(hey_list):
        if hey_object.id == id:
            return i
    raise ValueError("No such element")


def update(hey_object):
    index = __get_index(hey_object.id)
    hey_list[index] = hey_object
    write()


read()