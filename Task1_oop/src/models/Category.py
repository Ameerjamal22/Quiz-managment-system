from typing import List
from typing import Type
from src.Json.object_to_json_dict import ObjectJsonify



class Category(ObjectJsonify):

    def __init__(self, category_name: str, list_of_questions: List = []):
        """
        creates a new object from the Category class that has a name and a list of questions in it .
        ARGS:
            category_name (str) : the name of the category .
            list_of_questions (list) : the list of the questions that deecend under this category .
        """

        self.validate_creation(category_name)

        self.__category_name = category_name
        self.__list_of_questions = list_of_questions

    def get_category_name(self) -> str:
        """
        Gets the category name as a string .
        ARGS:
            self : the question object
        RETURNS:
            ( str ) : returns the question text for the question object as a string
        """
        return self.__category_name

    def get_list_of_questions(self) -> List:
        """
        gets the question textual representation as a string .
        ARGS:
            self : the question object
        RETURNS:
            ( str ) : returns the question text for the question object as a string
        """
        return self.__list_of_questions

    def validate_creation(self, category_name:str) -> bool:
        """
        check if the category name is valid ( non-empty ) .
        ARGS:
             category_name ( str ) : the name of the category passed as an argument for the constructor
        RETURNS:
            ( int ) : returns zero if the category name is valid , and a negative exist code if its not .
        """
        if not category_name:
            raise Exception("the category name should be non-empty")

    def jsonify_object(self) -> dict:
        """
        Converts the Category object into a JSON-compatible dictionary.
        Returns:
            dict: A dictionary representing the Category object.
        """

        return self.__category_name , [ question.jsonify_object() for question in self.__list_of_questions ]