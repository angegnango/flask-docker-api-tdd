import os
from api import db

def test_load_json_object_400():
    
    filesource = 'fake.json'
    response = db.load_json(filesource)
    assert response == f'File not found with the given path: {filesource}'


def test_load_json_object_200():

    filesource = f'{os.getcwd()}/database.json'
    response = db.load_json(filesource)
    assert isinstance(response, dict)


