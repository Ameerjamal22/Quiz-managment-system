
class InvalidCategoryCreation (Exception):
    """
    Exception class that represents invalid category creation
    """
    exit_code = 0

    @classmethod
    def handle(cls):
        """
        Handler for invalid category creation
        ARGS:
            exit_code ( int ) : indicates what is the problem in the creation of the category object .
        """
        global exit_code

        if exit_code == -1 :
            print ("Invalid category name the category name should be not null nor empty ")


