"""Module to generate python code, contains all functions."""

import os
import re
from collections import namedtuple
from enum import Enum
from pathlib import Path

from jinja2 import Environment, Template

PYTHON_CLASS = "python_class/class.py.jinja2"
CONSOLE_MODEL_CLASS = "console_app_class/console_model_cls.py.jinja2"
CONSOLE_UI_CLASS = "console_app_class/console_ui_cls.py.jinja2"
CONSOLE_MAIN_CLASS = "console_app_class/main_ui_cls.py.jinja2"
CONSOLE_USER_INPUT = "console_app_class/console.py"
FLASK_API = "flask/flask_api.py.jinja2"
TKINTER = "tkinter/tkinter.py.jinja2"

SQLALCHEMY_TYPES = {
    "int": "Integer",
    "str": "String",
    "float": "Float",
    "date": "Date",
    "bool": "Boolean"
}
HTML_TYPES = {
    "int": "number",
    "str": "text",
    "date": "date",
    "float": "number",
    "bool": "checkbox"
}
JAVA_TYPES = {
    "int": "Integer",
    "str": "String",
    "float": "Double",
    "date": "Date",
    "bool": "Boolean"
}
TKINTER_TYPES = {
    "int": "Entry",
    "str": "Entry"

}
C_TYPES = {
    "int": "int",
    "str": "char",
    "float": "double",
    "bool": "bool"

}
print(len("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"))
print(len("###############################################################################"))
###############################################################################


class Field:
    def __init__(self, data_type: str, name: str, primary_key=False, foreign_model: str = None):
        self.data_type = data_type
        self.name = name
        self.foreign_model = foreign_model  # as in foreign table, foreign key

    @property
    def html_type(self):
        return HTML_TYPES[self.data_type]

    @property
    def sqlalchemy_type(self):
        return SQLALCHEMY_TYPES[self.data_type]

    @property
    def java_type(self):
        return JAVA_TYPES[self.data_type]
    
    @property
    def tkinter_type(self):
        return TKINTER_TYPES[self.data_type]

    @property
    def name_p(self):  # pascal case like this PascalCaseClassName
        return "".join(map(str.capitalize, self.name.split("_")))

    @property
    def name_c(self):  # camel case, like this: camelCaseName
        parts = self.name.split("_")
        camel_case = parts[0].lower() + "".join(map(str.capitalize, parts[1:]))
        return camel_case

    @property
    def name_s(self):
        """ snake case - to be used in jinja template"""
        snake_name = re.sub('(?!^)([A-Z]+)', r'_\1', self.name).lower()
        return snake_name

    def __str__(self):
        return f"{self.name}"


class Model:
    def __init__(self, name: str, fields: list[Field]):
        self.name = name
        self.fields = fields
        self.relationship_models: list[Model] = []

    @property
    def name_p(self):  # pascal case like this PascalCaseClassName
        return "".join(map(str.capitalize, self.name.split("_")))

    @property
    def name_c(self):  # camel case, like this: camelCaseName
        parts = self.name.split("_")
        return parts[0].lower() + "".join(map(str.capitalize, parts[1:]))

    @property
    def name_s(self):  # snake case - we'll use it in jinja template, hence lower verbosity : D
        snake_name = re.sub('(?!^)([A-Z]+)', r'_\1', self.name).lower()
        return snake_name
    
    def __str__(self):
        return f"{self.name}"
 ###############################################################################


def render_code(template_filename, **kwargs):
    project_directory = Path(__file__).parent
    with open(f"{project_directory}/templates/{template_filename}", "r") as f:
        tm = Template(f.read())
        code = tm.render(**kwargs)

    return code


def generate_code(template_filename, output_filename, **kwargs):
    code = render_code(template_filename, **kwargs)
    project_directory = Path(__file__).parent
    with open(f"{project_directory}/examples/{output_filename}", "w") as f:
        f.write(code)


def generate_python_class(models):
    for model in models:
        generate_code(PYTHON_CLASS,
                      f"{model.name_s}_model.py",
                      model=model)


def generate_console_model_cls(models):
    for model in models:
        generate_code(CONSOLE_MODEL_CLASS,
                      f"{model.name_s}_model.py",
                      model=model)


def generate_console_ui_cls(models):
    for model in models:
        generate_code(CONSOLE_UI_CLASS,
                      f"{model.name_s}_ui.py",
                      model=model)


def generate_main_ui_cls(models):
    generate_code(CONSOLE_MAIN_CLASS,
                  "main.py",
                  models=models)


def generate_flask_api(models):
    generate_code(FLASK_API,
                  "api.py",
                  models=models)


def generate_flask_app(models):
    generate_code(
        "flask/flask.txt",
        "app.py",
        models=models)


def generate_index_html(models):
    generate_code("html/index.html",
                  "templates/index.html",
                  models=models)


def generate_base_html(models):
    generate_code("html/base.html", "templates/base.html",
                  models=models)


def generate_form_html(models):
    for model in models:
        generate_code("html/form.html", f"templates/{model.name}_form.html",
                      model=model)


def generate_profile_html(models):
    for model in models:
        generate_code("html/profile.html", f"templates/{model.name}_profile.html",
                      model=model)


def generate_table_html(models):
    for model in models:
        generate_code("html/table.html", f"templates/{model.name}_list.html",
                      model=model)


def generate_sqlalchemy_models(models):
    generate_code("sqlalchemy/sql.text", f"templates/models.py",
                  models=models)


def generate_tkinter_form(models):
    for model in models:
        generate_code(TKINTER, f"{model.name}.py",
                      model=model)


def generate_java_model(models):
    for model in models:
        for field in model.fields:
            if field.foreign_model:
                field.data_type = field.foreign_model
                field.name = field.foreign_model
                JAVA_TYPES[field.data_type] = field.foreign_model.capitalize()
    for model in models:
        generate_code("java/model.txt", f"{model.name.capitalize()}.java",
                      model=model)


def generate_java_repository(models):
    for model in models:
        generate_code("java/repository.txt", f"{model.name.capitalize()}Repository.java",
                      model=model)


def generate_console_input(models):
    generate_code(CONSOLE_USER_INPUT,
                  "console.py",
                  models=models)


def generate_full_flask(models):
    generate_index_html(models)
    generate_flask_app(models)
    generate_base_html(models)
    generate_form_html(models)
    generate_table_html(models)
    generate_profile_html(models)


def _get_code_generator(code_type):
    code_generators = {
        "console_model": generate_console_model_cls,
        "console_ui": generate_console_ui_cls,
        "console_main": generate_main_ui_cls,
        "flask_api": generate_flask_api,
        "flask_app": generate_flask_app,
        "base_html": generate_base_html,
        "full_flask": generate_full_flask,
        "java_model": generate_java_model,
        "java_repository": generate_java_repository,
        "python_class": generate_python_class,
        "console_input": generate_console_input,
        "tkinter_form": generate_tkinter_form
    }

    return code_generators[code_type]


models = []


def serialize(cls: type) -> Model:
    "Turns class into a model representation."
    fields = []
    foreign_models = []
    for field_name, field_type in cls.__annotations__.items():
        if "__" in field_name:
            field_name_pars, attribute = field_name.split("__")
            if "__pk" in field_name:
                field = Field(field_type.__name__,
                              field_name_pars, 
                              primary_key=True)
            else:
                for other_model in models:
                    if other_model.name.lower() == attribute.lower():
                        field = Field(field_type.__name__,
                                      field_name_pars, 
                                      foreign_model=other_model)
                        foreign_models.append(other_model)
                        break
                else:
                    raise ValueError(
                        f"Can't find {{ model }} model, try changing order.")

        else:
            field = Field(field_type.__name__, field_name)
        fields.append(field)

    model_name = cls.__name__
    model = Model(model_name, fields)
    #model.relationship_models = relationship_models

    return model


def parse(classes, code_type):
    """Loops through classes and generates files
    corresponding to the code type."""
    for cls in classes:
        models.append(serialize(cls))
    generator = _get_code_generator(code_type)
    generator(models)
    models.clear()


# IMPLEMENT ITERATOR
# IMPLEMENT FULL CONSOLE APP
# add - - - for names property
# implement foreign model in api
# implement logic of adding foreign models
# add underscore to global
# check __all__
#ADD TO PYTHON CLASSES DOCSTRING __all__
#SAY THAT _ doesnt import it
#TALK ABOUT NAME MANGLING