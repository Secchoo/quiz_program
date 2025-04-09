import os


def questions_getter():
    """Get a question from the user."""
    while True:
        # Prompt the user to enter a question
        question = input("\nEnter your question: ").strip()
        if question:
            # Return the question if it is not empty
            return question
        # Notify the user that the question cannot be empty
        print("Question cannot be empty!")


def choices():
    """Get four possible answers from the user."""
    letters = ['a', 'b', 'c', 'd']
    answers = []

    # Loop through each letter to get four answers
    for letter in letters:
        while True:
            # Prompt the user to enter an answer for the current letter
            answer = input(f"\nEnter answer ({letter}): ").strip()
            if answer:
                # Append the answer to the list if it is not empty
                answers.append(answer)
                break
            # Notify the user that the answer cannot be empty
            print("Answer cannot be empty!")
    # Return the list of answers
    return answers


def correct_answer(answers):
    """Get the correct answer from the user."""
    letters = ['a', 'b', 'c', 'd']

    while True:
        # Display the prompt to select the correct answer
        print("\nSelect the correct answer:")
        for letter, answer in zip(letters, answers):
            # Display each answer with its corresponding letter
            print(f"{letter}. {answer}")

        # Prompt the user to enter the letter of the correct answer
        choice = input("Enter the letter of the correct answer: ").lower().strip()
        if choice in letters:
            # Return the correct answer if the input is valid
            return choice
        # Notify the user of invalid input
        print("Invalid choice! Please enter a, b, c, or d.")


def quiz_question_saver(question, answers, correct_answer, filename="quiz_record.txt"):
    """Save the quiz data to a text file."""
    # Open the file in append mode
    with open(filename, 'a') as file:
        # Write the question to the file
        file.write(f"Question: {question}\n")

        # Write each answer with its corresponding letter
        letters = ['a', 'b', 'c', 'd']
        for letter, answer in zip(letters, answers):
            file.write(f"{letter}. {answer}\n")

        # Write the correct answer to the file
        file.write(f"Correct answer: {correct_answer}\n\n")


def edit_questions(filename="quiz_record.txt"):
    """Edit existing questions in the quiz."""
    # Check if the file exists and is not empty
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("\nNo questions available to edit!")
        return

    # Read all lines from the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    questions = []
    current_question = []

    # Group lines into individual questions
    for line in lines:
        if line.strip() == "":
            if current_question:
                questions.append(current_question)
                current_question = []
        else:
            current_question.append(line)
    if current_question:
        questions.append(current_question)

    # Display all questions for editing
    print("\n=== Edit Questions ===")
    for i, question in enumerate(questions, start=1):
        print(f"{i}. {question[0].strip()}")

    try:
        # Prompt the user to select a question to edit
        choice = int(input("\nEnter the number of the question to edit: ").strip())
        if 1 <= choice <= len(questions):
            selected_question = questions[choice - 1]
            print("\nEditing question:")
            print("".join(selected_question))

            # Get the updated question, answers, and correct answer
            new_question = questions_getter()
            new_answers = choices()
            new_correct_answer = correct_answer(new_answers)

            # Update the selected question
            updated_question = [f"Question: {new_question}\n"]
            letters = ['a', 'b', 'c', 'd']
            for letter, answer in zip(letters, new_answers):
                updated_question.append(f"{letter}. {answer}\n")
            updated_question.append(f"Correct answer: {new_correct_answer}\n\n")

            questions[choice - 1] = updated_question

            # Write the updated questions back to the file
            with open(filename, 'w') as file:
                for question in questions:
                    file.writelines(question)

            print("\nQuestion updated successfully!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def delete_questions(filename="quiz_record.txt"):
    """Delete existing questions from the quiz."""
    # Check if the file exists and is not empty
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("\nNo questions available to delete!")
        return

    # Read all lines from the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    questions = []
    current_question = []

    # Group lines into individual questions
    for line in lines:
        if line.strip() == "":
            if current_question:
                questions.append(current_question)
                current_question = []
        else:
            current_question.append(line)
    if current_question:
        questions.append(current_question)

    # Display all questions for deletion
    print("\n=== Delete Questions ===")
    for i, question in enumerate(questions, start=1):
        print(f"{i}. {question[0].strip()}")

    try:
        # Prompt the user to select a question to delete
        choice = int(input("\nEnter the number of the question to delete: ").strip())
        if 1 <= choice <= len(questions):
            # Remove the selected question
            del questions[choice - 1]

            # Write the remaining questions back to the file
            with open(filename, 'w') as file:
                for question in questions:
                    file.writelines(question)

            print("\nQuestion deleted successfully!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def display_menu():
    """Display the main menu with colors and emojis."""
    # ANSI escape codes for colors
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    # Print the menu with colors and emojis
    print(f"\n{CYAN}=== 🎉 Quiz Creator Menu 🎉 ==={RESET}")
    print(f"{GREEN}1️⃣  ➕ Add Question{RESET}")
    print(f"{YELLOW}2️⃣  👁️  View Questions{RESET}")
    print(f"{CYAN}3️⃣  ✏️  Edit Question{RESET}")
    print(f"{RED}4️⃣  🗑️  Delete Question{RESET}")
    print(f"{GREEN}5️⃣  ✅ Exit{RESET}")


def main():
    """Main function to run the quiz creator."""
    filename = "quiz_record.txt"

    # Welcome message for the user
    print("Welcome to Quiz Creator!")
    print("Add questions to your quiz. Press Ctrl+C to finish.")

    try:
        while True:
            # Display the main menu
            display_menu()

            # Prompt the user to select an option
            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == '1':
                # Add a new question to the quiz
                question = questions_getter()
                answers = choices()
                correct_answer_value = correct_answer(answers)
                quiz_question_saver(question, answers, correct_answer_value)
                print("\nQuestion added successfully!")
            elif choice == '2':
                # View all saved questions
                if os.path.exists(filename) and os.path.getsize(filename) > 0:
                    with open(filename, 'r') as file:
                        print("\n=== Available Questions ===")
                        print(file.read())
                else:
                    print("\nNo questions available!")
            elif choice == '3':
                # Edit an existing question
                edit_questions(filename)
            elif choice == '4':
                # Delete an existing question
                delete_questions(filename)
            elif choice == '5':
                # Exit the program
                print("\nQuiz creation completed!")
                print(f"All questions have been saved to {filename}")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")

    except KeyboardInterrupt:
        # Handle the user pressing Ctrl+C to exit
        print("\n\nQuiz creation completed!")
        print(f"All questions have been saved to {filename}")


if __name__ == "__main__":
    main()