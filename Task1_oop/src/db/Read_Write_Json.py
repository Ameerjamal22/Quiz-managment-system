import json
from src.Json.Json_Serializer import *

def read_json_data(file_name: str) -> dict :
    """
    reads the data from a json file given the file name
    ARGS:
         file_name ( str ) : the name of the json file that contains data .
    RETURNS:
          ( dict) : return a dictionary that contains the data in the json file .
    """

    with open(file_name, "r") as data_file:
        data = json.loads(data_file.read())
        return data


def write_json_data(file_name:str, data:dict ) -> None:

    """
    writes the json dict as json string into the json file
    Args:
        file_name: the json file name that the json data will be written to
        data: the json data (dict) that will be written to the json file
    """
    with open("data.json", 'w') as data_file:
        json.dump( data , data_file, indent=2)