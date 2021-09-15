# CRUD Code Generator

Generates models, views and controllers for console, gui and web apps.

# How to use it?

Create classes with fields and their annotations. 
Pass a list of those classes to parse function and specify what code you want to generate.

```
from crud_code_generator import parse

class Person:
    name: str
    age: int

class Product:
    name: str
    price: float

parse([Person, Product], "flask_api")
```

# About 
Created by Darko Dekan.

