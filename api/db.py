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



