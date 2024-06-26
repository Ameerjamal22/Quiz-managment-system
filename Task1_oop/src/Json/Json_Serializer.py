from src.models.Question import Question
from src.models.Category import Category
from typing import List
from typing import Type
import json


def get_category_names_from_json(json_data: dict) -> List[str]:
    '''
    gets the category names from the json dict
    ARGS:
        json_data ( dict ) : the dictionary that contains the data read from the json file .
    Return:
        ( list ) : returns a list of all the categories in the json file .
    '''

    category_names = []

    for categories in json_data:
        category_names.append(categories)

    return category_names


def read_json_categories_data(json_data: dict) -> List[Category]:
    '''
    Convert the json dictionary that contains data into a list of category objects .
    ARGS:
        json_data (dict) : a dictionary that contains the categories with all their data .
    RETURNS:
        ( list ) : returns a list of categories objects converted from json dict into objects .
    '''
    categories = []

    for category_name, list_of_questions in json_data.items():

        current_category_questions = []

        for question in list_of_questions:
            question_text = question["question"]
            options_list = question["options"]
            correct_option = question["answer"]
            new_question = Question(question_text, options_list, correct_option)

            current_category_questions.append(new_question)

        categories.append(Category(category_name, current_category_questions))

    return categories


def convert_categories_to_json_dict(list_of_categories: List[Category]) -> dict:
    """
    converts a list of categories objects passed as a parameter into a json dict
    Args:
        list_of_categories : list of categories objects to be converted .

    Returns:
        a json dict representing the categories .
    """

    json_dict = {}

    for category in list_of_categories:

        list_of_question = []
        for question in category.get_list_of_questions() :
            list_of_question.append(question.to_json())

        json_dict[category.get_category_name()] = list_of_question

    return json_dict
