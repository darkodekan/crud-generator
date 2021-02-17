from crud_code_generator import model

@model
class Person:
    name: str
    age: int

@model
class Product:
    name: str
    price: float
    
