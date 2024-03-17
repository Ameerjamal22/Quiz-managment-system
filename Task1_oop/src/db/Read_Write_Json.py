import json


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



