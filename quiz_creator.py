def questions_getter():
    """ This function is responsible for getting questions from the user."""

    #prompts the user to enter a question
    question = input("Enter the question: ")

    #makes sure that the question is not empty
    if question == "":
        print("Question cannot be empty.")
        return questions_getter()
    
    #makes sure that the input is a sentence
    if not question.endswith("?"):
        print("Question must be a sentence.")
        return questions_getter()

def choices():
    """ This function is responsible for getting choices from the user."""

    #prompts the user to enter the choices
    choice1 = input("Enter choice 1: ")
    choice2 = input("Enter choice 2: ")
    choice3 = input("Enter choice 3: ")
    choice4 = input("Enter choice 4: ")

    #makes sure that the choices are not empty
    if choice1 == "" or choice2 == "" or choice3 == "" or choice4 == "":
        print("Choices cannot be empty.")
        return choices()

def correct_answer():
    """ This function is responsible for getting the correct answer from the user."""

def quiz_question_saver():
    """ This function is responsible for saving the quiz question to the text file."""

def main_menu():
    """ This function is responsible for displaying the main menu."""