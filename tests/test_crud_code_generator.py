import crud_code_generator as code_gen
import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def klasa():
    class Product:
        name: str
        price: float
    return Product

@pytest.fixture 
def classes():
    from datetime import date
    class User:
        username: str
        password: str
        age: int
    class Post:
        title: str 
        content: str
        published: date
    classes = [User, Post]
    return classes

@pytest.fixture
def model():
    field1 = code_gen.Field("int", "id")
    field2 = code_gen.Field("str", "name")
    model = code_gen.Model("person", [field1, field2])
    return model

def test_field():
    field = code_gen.Field("int", "price_food")
    field1 = code_gen.Field("str", "food")
    print(field1.name_c)
    print(field1.name_s)
    assert field.name_c == "priceFood"
    assert field.name_p == "PriceFood"
    assert field.name_s == "price_food"
    
    assert field1.name_c == "food"

def test_model():
    field1 = code_gen.Field("date", "price_food")
    field2 = code_gen.Field("str", "hobby")
    model = code_gen.Model("example", [field1, field2])
    assert model.name == "example"
    assert model.name_p == "Example"
    assert field1.name == "price_food"


def test_render_code(model):
    result1 = code_gen.render_code(code_gen.CONSOLE_MAIN_CLASS, models=[model])
    result2 = code_gen.render_code(code_gen.CONSOLE_MODEL_CLASS, model=model)
    result3 = code_gen.render_code(code_gen.CONSOLE_UI_CLASS, model=model)
    result4 = code_gen.render_code(code_gen.FLASK_APP, models = [model])

    assert model.fields[0].data_type in result1
    assert model.fields[1].name_s in result2
    assert model.fields[0].name_c in result3
    assert model.name_c in result4
    print(model.fields[0].name_c.upper())


def test__get_code_generators():
    generator = code_gen._get_code_generator("full_flask")
    assert generator.__name__ == "generate_full_flask"


def test_serialize(klasa):
    model = code_gen.serialize(klasa)
    assert model.name == "Product" and model.fields[0].data_type == "str"
