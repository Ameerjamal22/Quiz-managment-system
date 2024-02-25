
from src.errors.InvalidCategoryCreation import InvalidCategoryCreation
class Category :

    def __init__( self , category_name , list_of_questions = [] ):
        """
        creates a new object from the Category class that has a name and a list of questions in it .
        ARGS:
            category_name (str) : the name of the category .
            list_of_questions (list) : the list of the questions that deecend under this category .
        """

        exit_code = Category.is_valid_category_name( category_name )

        if exit_code != 0 :

            InvalidCategoryCreation.exit_code = exit_code
            raise InvalidCategoryCreation("An error occurred during the category creation :")

        self.__category_name = category_name
        self.__list_of_questions = list_of_questions

    def get_category_name( self ) :
        """
        Gets the category name as a string .
        ARGS:
            self : the question object
        RETURNS:
            ( str ) : returns the question text for the question object as a string
        """
        return self.__category_name

    def get_list_of_questions( self ):
        """
        gets the question textual representation as a string .
        ARGS:
            self : the question object
        RETURNS:
            ( str ) : returns the question text for the question object as a string
        """
        return self.__list_of_questions

    def is_valid_category_name(category_name):
        """
        check if the category name is valid ( non-empty ) .
        ARGS:
             category_name ( str ) : the name of the category passed as an argument for the constructor
        RETURNS:
            ( int ) : returns zero if the category name is valid , and a negative exist code if its not .
        """
        if category_name:
            return 0
        else:
            return -1
