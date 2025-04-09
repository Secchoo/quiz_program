def questions_getter():
    """This function is responsible for getting questions from the user."""
    
    # Prompt the user to enter a question
    while True:
        question = input("\nEnter the question: ")
        if question:
            return question
        print("Question cannot be empty.")


def choices():
    """This function is responsible for getting choices from the user."""
    
    # Prompt the user to enter the choices
    answers = []
    for i in range(4):
        while True:
            answer = input(f"Enter choice {i + 1}: ")
            if answer:
                answers.append(answer)
                break
            print("Choice cannot be empty.")
    return answers


def correct_answer(answers):
    """This function is responsible for getting the correct answer."""
    
    while True:
        print("\nSelect the correct answer for the question:")
        for i, answer in enumerate(answers):
            print(f"{i + 1}. {answer}")
        choice = input("Enter the number of the correct answer: ")
        if choice.isdigit() and 1 <= int(choice) <= len(answers):
            return int(choice)
        print("Invalid choice. Please enter a valid number.")


def quiz_question_saver():
    """This function saves the quiz question to a text file."""
    
    question = questions_getter()
    answers = choices()
    correct_answer_choice = correct_answer(answers)

    # Save the question and answers to a text file
    with open("quiz_record.txt", "a") as f:
        f.write(f"Question: {question}\n")
        for i, answer in enumerate(answers):
            f.write(f"Choice {i + 1}: {answer}\n")
        f.write(f"Correct Answer: Choice {correct_answer_choice}\n\n")

    print("Quiz question saved successfully!")


def main_menu():
    """This function displays the main menu."""
    
    print("Welcome to the Quiz Creator!")
    print("1. Create a new quiz question")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    """Main function to run the quiz creator."""

    filename = "quiz_record.txt"

    print("Welcome to the Quiz Creator!")

    try:
        while True:
            question = questions_getter()
            answers = choices()
            correct_answer_choice = correct_answer(answers)
            quiz_question_saver(question, answers, correct_answer_choice)
            print("Quiz question saved successfully!")

    except KeyboardInterrupt:
        print("\nExiting the quiz creator.")
        print(f"all questions are saved in quiz_record.txt")

if __name__ == "__main__":
    main()