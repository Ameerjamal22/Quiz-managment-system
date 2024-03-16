from typing import List
from src.Json.object_to_json_dict import Object_Jsonify




class Question(Object_Jsonify):
    '''
    Question class used as a question holder contains :
    1 - question_text (str) : textual representation of the question .
    2 - options_list (list) : list of options for the questions stored as strings .
    3 - correct_option (str) : the correct answer (option) for the question .
    '''

    def __init__(self, question_text: str, options_list: List[str], correct_option: str) :
        '''
        creates a question object .
        ARGS:
            question_text (str): Textual representation of the question .
            options_list (list): List of strings where each element stands for an option of the question .
            correct_option (str):string that stands for correct answer .
        RETURNS:
            Question object .
        '''

        self.validate_creation(question_text, options_list, correct_option)

        self.__question_text = question_text
        self.__options_list = options_list
        self.__correct_option = correct_option

    def get_question_text(self) -> str:
        """
        gets the question textual representation as a string .
        ARGS:
            self : the question object
        RETURNS:
            ( str ) : returns the question text for the question object as a string
        """
        return self.__question_text

    def get_options_list(self) -> List[str]:
        """
        Gets the options list of the question
        ARGS:
            self : the question object
        RETURNS:
            ( List of string ) where each element stands for an option of the) :
        """

        return self.__options_list

    def get_correct_option(self) -> str:
        """
        gets the question textual representation as a string .
        ARGS:
            self : the question object
        RETURNS:
            ( str ) : returns the question text for the question object as a string
        """

        return self.__correct_option

    def is_correct_answer_in_options(self, correct_option:str, options_list:List[str]) -> bool:
        '''
        check is the correct answer exist in the list of options .
        ARGS:
             correct_option ( str ) : correct answer .
             option_list (list) : list of question options .
        RETURNS:
             ( bool ): True if the correct answer is one of the options and False otherwise .
        '''
        return correct_option in options_list

    def is_question_text_empty(self, question_text:str) -> bool:
        '''
        check is the question text is empty or null , returns True if yes , False if no .
        ARGS:
             question_text (str): question string
        RETURNS:
             ( bool ) : returns True if the text question is empty or None False otherwise  .
        '''
        return question_text == "" or question_text == None

    def is_valid_number_of_options(self, options_list:List[str]) -> bool :
        '''
        check if the number of options in the list of options is valid .
        ARGS:
             option_list (list) : list of question options .
        RETURNS:
             ( bool ): Ture is valid False otherwise  .
        '''
        return len(options_list) == 4

    def is_valid_question_attr_type(self, question_text:str, options_list:List[str], correct_option:str) -> bool :
        '''
        check if tha passed argument has the appropriate type .
        ARGS:
            question_text (str): question statement .
            option_list (list) : list of question options .
            correct_option ( str ) : correct answer .
        RETURNS:
            ( bool ): True if the correct answer is one of the options and False otherwise .
        '''
        return type(question_text) == str and type(options_list) == list and type(correct_option) == str

    def validate_creation(self, quesiton_text:str, options_list:List[str], correct_option:str) -> bool:
        """
        check if all the constraints are met  for the creation of a Question object .
        ARGS:
            question_text (str): question statement .
            option_list (list) : list of question options .
            correct_option ( str ) : correct answer .
        RETURNS:
            ( int ): returns 0 if all constraints are met and non zero exit code otherwise .
        """
        if not self.is_valid_number_of_options(options_list):
            raise Exception("Number of options should be exactly four options")

        if not self.is_correct_answer_in_options(correct_option, options_list):
            raise Exception("The input answer should be one of the input options ")

        if self.is_question_text_empty(quesiton_text):
            raise Exception("The question statement should be non empty")

        if not self.is_valid_question_attr_type(quesiton_text, options_list, correct_option):
            raise Exception("check that you enetered a correct type for each input")

    def jsonify_object(self) -> dict:
        """
        Converts the Question object into a JSON-compatible dictionary.
        Returns:
            dict: A dictionary representing the Question object.
        """

        return {
            "question": self.__question_text,
            "options": self.__options_list,
            "answer": self.__correct_option
        }
