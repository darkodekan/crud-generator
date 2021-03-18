from datetime import date

from crud_code_generator import parse


class Customer:
    id__pk: int
    name_pers: str
    AgesAll: int
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
#parse([Customer, Item, Hey], "console_model")
#parse([Customer, Item, Hey], "console_ui")
#parse([Customer, Item, Hey], "console_main")
#parse([Customer, Item, Hey], "console_input")
parse([Customer, Item, Hey], "tkinter_form")


# parse([Customer, Item, Hey], "console_main")


# USE ENUM
