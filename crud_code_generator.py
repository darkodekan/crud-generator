from jinja2 import Template, Environment
from collections import namedtuple
from enum import Enum




class Field:
    def __init__(self, data_type: str, name: str):
        self.data_type = data_type
        self.name = name
 


class Model:
    def __init__(self, name: str, fields: list[Field]):
        self.name = name
        self.fields = fields 

class SQLAlchemyField(Field):
    db_types = {"int":"Integer",
            "str":"String",
            "float":"Float",
            "date":"Date"}
   

    def __init__(self, data_type: str, name: str, key=None, foreign_table=None):
        super().__init__(data_type, name)
        self.db_type =  SQLAlchemyField.db_types[data_type]
        self.key = key
        self.foreign_table = foreign_table
    def __str__(self):
        return f"{self.data_type} {self.name} {self.key}"

Key = Enum('Key', 'PRIMARY FOREIGN')


class HTMLField(Field):
    pass

import sys

def create_model(model_string):
    model_name, fields_str = model_string.split(",")
    fields = []
    for field_str in fields_str.split():
        elements = field_str.split(":")
        if len(elements) == 2:
            name, type_name = elements
            field = SQLAlchemyField(type_name, name)
        elif len(elements) == 3:
            name, type_name, key = elements
            key = Key.PRIMARY 
            field = SQLAlchemyField(type_name, name, key=key)
        elif len(elements) == 4:
            name, type_name, key, foreign_table = elements
            field = SQLAlchemyField(type_name, name, Key.FOREIGN, foreign_table=foreign_table)
        else:
            raise ValueError("Wrong number of variables")

        fields.append(field)
        print(field)
        key = None
    return Model(model_name, fields)

models = []
def create_models(model_strings):
    for m in model_strings:
        models.append(create_model(m))
  

def generate_code(template_filename, output_filename, **kwargs):
    with open(f"templates/{template_filename}", "r") as f:
        tm = Template(f.read())
        result = tm.render(**kwargs)
        with open(f"examples/{output_filename}", "w") as model_file:
            model_file.write(result)

#profile_id = db.Column(db.Integer, db.ForeignKey(Profile.id)) 
#print(sys.argv)
model_strings = sys.argv[1:]
print(model_strings)

create_models(model_strings)

def generate_sqlalchemy_model_code():
    generate_code("sql.txt", "models.py", models=models)

def generate_class_model_code():
    generate_code("class_based_console/console_class_model_template.txt", "user_model.py", model=models[0])


def generate_class_controller_code():
    generate_code("class_based_console/console_controller_template.txt", "user_controller.py", model=models[0])


def generate_table_html_code():
    generate_code("table.html", "table.html", model=models[0])


def generate_table_html_code():
    generate_code("form.html", "form.html", model=models[0])

"""
#generate_sqlalchemy_model_code()

generate_class_model_code()
#generate_class_view_code()
generate_class_controller_code()


generate_sqlalchemy_model_code()

generate_table_html_code()
"""

def model(cls):
    fields = []
    for field_name, field_type in cls.__annotations__.items():
        field = Field(field_type.__name__, field_name)
        fields.append(field)
    model = Model(cls.__name__.lower(), fields)
    generate_code("class_based_console/console_class_model_template.txt", f"{model.name}_add.py", model=model)
    return cls


    



