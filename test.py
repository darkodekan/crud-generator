from datetime import date

from crud_code_generator import parse


class Customer:
    id__pk: int
    name_pers: str
    AgesAll__item: int
    hobby: bool
    heh: bool


class Item:
    id__pk: int
    name: str
    price: float
    customer_id__customer: int
    asd: str


class Hey:
    id__pk: int
    price: float
    asd: str
    uff: str


# parse([Customer, Item], "java_repository")
parse([Customer, Item, Hey], "console_model")
parse([Customer, Item, Hey], "console_ui")
parse([Customer, Item, Hey], "console_main")
parse([Customer, Item, Hey], "console_input")
#parse([Customer, Item, Hey], "tkinter_form")


class Osoba:
    id__pk: int
    ime: str
    prezime: str

class Zadatak:
    id__pk: int
    opis: str
    osoba__osoba: int

parse([Osoba, Zadatak], "flask_api")


# USE ENUM
