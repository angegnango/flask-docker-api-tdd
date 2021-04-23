import requests

def retrieve_city(search_key:str):

    """ handler to return city of the given query string 
    param(str) : search key 
    return(str) : city
    """
    
    url = f'https://api-adresse.data.gouv.fr/search/?q={search_key}'

    execute_request = requests.get(url)
    response = execute_request.json()

    if len(response['features'])>0:
        return response['features'][0]['properties']['city']
    else:
        return None
