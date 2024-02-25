
from src.models.Question import Question
from src.models.Category import Category


def get_category_names_from_json ( json_data ):
    '''
    gets the category names from the json dict
    ARGS:
        json_data ( dict ) : the dictionary that contains the data read from the json file .
    Return:
        ( list ) : returns a list of all the categories in the json file .
    '''

    category_names = []

    for categories in json_data :
        category_names.append( categories )

    return category_names


def convert_dict_into_question_object ( question_dict ):
    '''
    converts the question dictionary into a Question object
    ARGS:
        question_dict (dict) : question representation as a dict
    RETURNS:
        returns a question object ( object representation of the question passed as dictionary )
    '''

    question_text = str( question_dict["question"] )
    options_list = list(question_dict["options"])
    correct_option = str(question_dict["answer"])

    return Question( question_text, options_list , correct_option )




def read_json_categories_data( json_data ):
    '''
    Convert the json dictionary that contains data into a list of category objects .
    ARGS:
        json_data (dict) : a dictionary that contains the categories with all their data .
    RETURNS:
        ( list ) : returns a list of categories objects converted from json dict into objects .
    '''

    category_names = get_category_names_from_json(json_data)
    categories = []

    for category_name in category_names :

        list_of_questions_for_current_category = json_data[category_name]
        category_list_of_questions = []

        for question in list_of_questions_for_current_category :

            category_list_of_questions.append(convert_dict_into_question_object(question))


        categories.append( Category( category_name, category_list_of_questions ) )

    return categories



