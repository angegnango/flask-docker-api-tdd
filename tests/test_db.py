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


def test_database_contain_brest_200():

    filesource = f'{os.getcwd()}/database.json'
    response = db.load_json(filesource)
    assert 'Brest' in response


def test_database_not_contain_paris_404():
    
    filesource = f'{os.getcwd()}/database.json'
    response = db.load_json(filesource)
    assert not 'Paris' in response


def test_paris_network_coverage_404():

    city = 'Paris'
    response = db.search(city)
    assert response == f'{city} not found in our current database'


def test_brest_network_coverage_200():

    city = 'Brest'
    response = db.search(city)
    assert isinstance(response, dict)
    assert 'orange' in response
    assert 'SFR' in response
    assert 'Free' in response
    assert 'Bouygues Telecom' in response


def test_brest_is_covered_by_all_operator_200():
    
    city = 'Brest'
    response = db.search(city)
    assert 'orange' in response
    assert 'SFR' in response
    assert 'Free' in response
    assert 'Bouygues Telecom' in response


def test_brest_details_200():
    
    city = 'Brest'
    response = db.search(city)
    assert response['orange']== ['2G','3G', '4G']
    assert response['Free']== ['3G', '4G']
    assert response['SFR']== ['2G','3G', '4G']
    assert response['Bouygues Telecom']== ['2G','3G', '4G']