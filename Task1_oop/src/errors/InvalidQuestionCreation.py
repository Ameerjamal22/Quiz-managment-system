class InvalidQuestionCreation (Exception) :
    """
    Exception class that represents invalid question creation
    """
    exit_code = 0

    @classmethod
    def handle( cls ) :
        """
        Handler for invalid question creation
        ARGS:
            exit_code ( int ) : indicates what is the problem in the creation of the question object .
        """

        global exit_code

        if exit_code == -1 :
            print( "The number of question options should be 4 ")
        elif exit_code == -2 :
            print("The correct answer should be one of the options")
        elif exit_code == -3 :
            print("Question text cannot be empty or null ")
        elif exit_code == -4 :
            print("check if the attribute is correct")
