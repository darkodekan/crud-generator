# CRUD Code Generator

Generates models, views and controllers for console, gui and web apps.


# Configuration
There is no need to use configure it.


# How to use it?

You can generate HTML forms, Tkinter GUIs, Models etc. this way.
Create class with fields and annotate them:


```
from code_generator import register, generate

@register
class User:
    int: id
    email: str
    name: str

@regiser
class Product:
    int: id
    name: str
    price: float

generate()
```




How to run it?
crud_gen --console-class-view "Product, int:name str:name"

Creates view for console. Example code.


crud_gen --console-class-view "Product, int:name str:name"

crud_gen --full-console 

# Contributing



# About 
Created by Darko Dekan.

