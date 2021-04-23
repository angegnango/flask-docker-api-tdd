from api import handler

def test_retrieve_11_rue_petit_city():

    query = '11 rue petit'
    response = handler.retrieve_city(query)
    assert response == 'Paris'