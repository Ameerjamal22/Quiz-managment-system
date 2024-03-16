from src.db.Read_Write_Json import *
from src.Json.Json_Serializer import *


def display_options(username):
    """
    displays the program menu .
    """
    print("Hello  " + username + "  !")
    print("""

    Enter a number to determine your choice :
    1 - Test yourself with a quiz 
    2 - create a new quiz category
    3 - create a new question in one of the categories    
    4 - exit
    """)


def read_tests_data(file_name):
    """
    reads data from json and returns a list of categories object . .
    """

    json_dict = read_json_data(file_name)
    list_of_categories = read_json_categories_data(json_dict)
    return list_of_categories


def print_category_options(list_of_categories, username):
    print(f" {username} please enter your choice for the category that you want to be tested in ")

    for index, category in enumerate(list_of_categories):
        print(index + 1, " : " + category.get_category_name())

    choice = input("")

    if 1 <= int(choice) <= len(list_of_categories):
        return list_of_categories[int(choice) - 1]
    else:
        return print_category_options(list_of_categories, username)


def initiate_quiz(username, list_of_categories):
    """
    initiates the quiz with the category that the user choose ,and keep giving
    question until the category question end or the user want to stop .
    ARGS:
        username ( str ) : the name of the program user .
        list_of_categories ( list ) : the list of category objects that contain the categories .
    """

    category_choice = print_category_options(list_of_categories, username)
    grade = 0

    for question in category_choice.get_list_of_questions():

        print(question.get_question_text())

        for index, option in enumerate(question.get_options_list()):
            print(index + 1, "- ", option)

        user_answer = input("Enter your options from 1 - 4 :")

        if question.get_options_list()[int(user_answer) - 1] == question.get_correct_option():
            grade += 1
            print("the answer is correct !")

        else:
            print("your answer is incorrect")
            print("correct option :" + question.get_correct_option())

    print("You got " + str(grade) + " out of " + str(
        len(category_choice.get_list_of_questions())) + " good job ." + username)


def create_category_by_user_inputs(list_of_categories):
    """
    creates a new category with no questions in it .
    ARGS:
        list_of_categories ( list ) : the list of categories
    RETURNS:
        updated list of categories .
    """
    category_name = input("Enter the name of the new category that you want to create:")

    category_name_exist = False

    for category in list_of_categories:

        if category.get_category_name() == category_name:
            category_name_exist = True
            break

    if category_name_exist:
        print("The entered name already exists , exiting")

    else:
        new_category = Category(category_name)
        list_of_categories.append(new_category)
        print("category added successfully")

    return list_of_categories


def options_handler(choice, username, list_of_categories):
    """
    handles the menu options based on the user choice
    ARGS:
        choice (string) : choice of the user as a string
        username (string) :the username of the current user that is using the program.
        list_of_categories ( list ) : list of the available categories objects .
    Returns:
        ( bool ) : returns a boolean that indicates of the user wants to exit the program or not .
    """
    if choice == '1':
        initiate_quiz(username, list_of_categories)

    elif choice == '2':
        list_of_categories = create_category_by_user_inputs(list_of_categories)

    elif choice == '3':
        add_question_to_category(list_of_categories)

    elif choice == '4':
        return True
    else:
        print("invalid option")
        return False


def quiz_menu(file_name, user_name):
    """
    the main driver function of the quiz program controls the flow of the program
    ARGS:
        file_name (string) : the name of the json file that contain the data .
        username (string) :the username of the current user that is using the program.
    Returns:
        ( bool ) : returns a boolean that indicates of the user wants to exit the program or not .
    """
    list_of_categories = read_tests_data(file_name)
    choice = '-1'

    while choice != '4':

        display_options(user_name)
        choice = input("")

        try:
            exit = options_handler(choice, user_name, list_of_categories)
            if exit:
                break

        except Exception as E:
            print(f"An error occurred : {E.args}")

    print(f" {user_name} Thank you for using the program , best regards")


def create_new_question_by_user(list_of_categories, choice):
    """
    creates a new question and add it to the category specified by the user .
    Args:
        list_of_categories ( list of strings ): list of categories .
        choice ( int ) : the number of the category that the newly created question will be added to .

    Returns:
        ( list of strings) : the updated list of categories after the question is added .
    """

    question_text = input("Enter your question statement")

    options_list = []

    for i in range(4):
        options_list.append(input(f"Enter the {i + 1} option"))

    correct_option = input("Enter the correct answer ( should be one of the question options )")
    list_of_categories[choice].get_list_of_questions().append(Question(question_text, options_list, correct_option))

    return list_of_categories


def add_question_to_category(list_of_categories):
    """
    handles the ( create a new question in one of the categories ) option .
    Args:
        list_of_categories ( list of strings ): list of categories .

    Returns:
        ( list of strings) : the updated list of categories after the question is added .
    """

    print("choose the category you want to add a questions to :")

    for category in list_of_categories:
        print(category.get_category_name())

    choice = ""

    while True:

        choice = input("Enter your choice :")
        choice = int(choice)

        if 0 <= choice <= len(list_of_categories):
            break
        else:
            print("Enter one of the valid choices")

    list_of_categories = create_new_question_by_user(list_of_categories, choice - 1)
    return list_of_categories


if __name__ == "__main__":
    quiz_menu("data.json", "ameer")
