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

def correct_answer():
    """ This function is responsible for getting the correct answer from the user."""

def quiz_question_saver():
    """ This function is responsible for saving the quiz question to the text file."""

def main_menu():
    """ This function is responsible for displaying the main menu."""