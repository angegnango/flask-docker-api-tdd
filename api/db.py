import os
import json


def load_json(filesource:str):

    """ handler to return json object as python dict 
    param(str) : json filepath 
    return (dict) : dictionnary 
    """

    if os.path.isfile(filesource):
        
        with open(filesource, 'r') as json_file:
            return json.load(json_file)
    else:
        return f'File not found with the given path: {filesource}'



def search(city:str):

    """ handler to return network coverage for the given city
    param(str) : city
    return (dict) or (str) response object
    """

    filesource = f'{os.getcwd()}/database.json'
    error_message = f'{city} not found in our current database'
    dataset = load_json(filesource)

    return dataset.get(city, error_message)

