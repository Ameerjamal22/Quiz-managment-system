from src.errors.InvalidQuestionCreation import InvalidQuestionCreation
class Question:

    '''
    Question class used as a question holder contains :
    1 - question_text (str) : textual representation of the question .
    2 - options_list (list) : list of options for the questions stored as strings .
    3 - correct_option (str) : the correct answer (option) for the question .
    '''

    def __init__(self , question_text , options_list , correct_option ):
        '''
        creates a question object .
        ARGS:
            question_text (str): Textual representation of the question .
            options_list (list): List of strings where each element stands for an option of the question .
            correct_option (str):string that stands for correct answer .
        RETURNS:
            Question object .
        '''

        exit_code = Question.is_valid_creation_call(question_text , options_list , correct_option)

        if exit_code != 0 :

            InvalidQuestionCreation.exit_code = exit_code
            raise InvalidQuestionCreation("An error occurred in the creation of question object:")

        self.__question_text = question_text
        self.__options_list = options_list
        self.__correct_option = correct_option


    def get_question_text (self):
        """
        gets the question textual representation as a string .
        ARGS:
            self : the question object
        RETURNS:
            ( str ) : returns the question text for the question object as a string
        """
        return self.__question_text

    def get_options_list (self):

        return self.__options_list


    def get_correct_option (self):
        """
        gets the question textual representation as a string .
        ARGS:
            self : the question object
        RETURNS:
            ( str ) : returns the question text for the question object as a string
        """
        return self.__correct_option


    def is_correct_answer_in_options(correct_option, options_list):
        '''
        check is the correct answer exist in the list of options .
        ARGS:
             correct_option ( str ) : correct answer .
             option_list (list) : list of question options .
        RETURNS:
             ( bool ): True if the correct answer is one of the options and False otherwise .
        '''
        return correct_option in options_list


    def is_question_text_empty(question_text):
        '''
        check is the question text is empty or null , returns True if yes , False if no .
        ARGS:
             question_text (str): question string
        RETURNS:
             ( bool ) : returns True if the text question is empty or None False otherwise  .
        '''
        return question_text == "" or question_text == None


    def is_valid_number_of_options(options_list):
        '''
        check if the number of options in the list of options is valid .
        ARGS:
             option_list (list) : list of question options .
        RETURNS:
             ( bool ): Ture is valid False otherwise  .
        '''
        return len(options_list) == 4


    def is_valid_question_attr_type(question_text, options_list, correct_option):
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


    def is_valid_creation_call(quesiton_text, options_list, correct_option):
        """
        check if all the constraints are met  for the creation of a Question object .
        ARGS:
            question_text (str): question statement .
            option_list (list) : list of question options .
            correct_option ( str ) : correct answer .
        RETURNS:
            ( int ): returns 0 if all constraints are met and non zero exit code otherwise .
        """
        if Question.is_valid_number_of_options(options_list) == False:
            return -1

        elif Question.is_correct_answer_in_options(correct_option, options_list) == False:
            return -2

        elif Question.is_question_text_empty(quesiton_text) == True:
            return -3

        elif Question.is_valid_question_attr_type(quesiton_text, options_list, correct_option) == False:
            return -4

        else:
            return 0