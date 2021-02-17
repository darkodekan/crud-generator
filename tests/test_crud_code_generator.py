import crud_code_generator
def test_create_model():
    result = crud_code_generator.create_model("user, id:int:pk name:str")
    assert result.name == "user" and result.fields[0].name == "id"

