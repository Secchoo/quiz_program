import os


def questions_getter():
    """Get a question from the user."""
    while True:
        question = input("\nEnter your question: ").strip()
        if question:
            return question
        print("Question cannot be empty!")


def choices():
    """Get four possible answers from the user."""
    letters = ['a', 'b', 'c', 'd']
    answers = []

    for letter in letters:
        while True:
            answer = input(f"\nEnter answer ({letter}): ").strip()
            if answer:
                answers.append(answer)
                break
            print("Answer cannot be empty!")
    return answers


def correct_answer(answers):
    """Get the correct answer from the user."""
    letters = ['a', 'b', 'c', 'd']

    while True:
        print("\nSelect the correct answer:")
        for letter, answer in zip(letters, answers):
            print(f"{letter}. {answer}")

        choice = input("Enter the letter of the correct answer: ").lower().strip()
        if choice in letters:
            return choice
        print("Invalid choice! Please enter a, b, c, or d.")


def quiz_question_saver(question, answers, correct_answer, filename="quiz_record.txt"):
    """Save the quiz data to a text file."""
    with open(filename, 'a') as f:
        f.write(f"Question: {question}\n")
        letters = ['a', 'b', 'c', 'd']
        for letter, answer in zip(letters, answers):
            f.write(f"{letter}. {answer}\n")
        f.write(f"Correct answer: {correct_answer}\n\n")


def edit_questions(filename="quiz_record.txt"):
    """Edit existing questions in the quiz."""
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("\nNo questions available to edit!")
        return

    with open(filename, 'r') as f:
        lines = f.readlines()

    questions = []
    current_question = []
    for line in lines:
        if line.strip() == "":
            if current_question:
                questions.append(current_question)
                current_question = []
        else:
            current_question.append(line)
    if current_question:
        questions.append(current_question)

    print("\n=== Edit Questions ===")
    for i, question in enumerate(questions, start=1):
        print(f"{i}. {question[0].strip()}")

    try:
        choice = int(input("\nEnter the number of the question to edit: ").strip())
        if 1 <= choice <= len(questions):
            selected_question = questions[choice - 1]
            print("\nEditing question:")
            print("".join(selected_question))

            new_question = questions_getter()
            new_answers = choices()
            new_correct_answer = correct_answer(new_answers)

            updated_question = [f"Question: {new_question}\n"]
            letters = ['a', 'b', 'c', 'd']
            for letter, answer in zip(letters, new_answers):
                updated_question.append(f"{letter}. {answer}\n")
            updated_question.append(f"Correct answer: {new_correct_answer}\n\n")

            questions[choice - 1] = updated_question

            with open(filename, 'w') as f:
                for question in questions:
                    f.writelines(question)

            print("\nQuestion updated successfully!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def delete_questions(filename="quiz_record.txt"):
    """Delete existing questions from the quiz."""
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("\nNo questions available to delete!")
        return

    with open(filename, 'r') as f:
        lines = f.readlines()

    questions = []
    current_question = []
    for line in lines:
        if line.strip() == "":
            if current_question:
                questions.append(current_question)
                current_question = []
        else:
            current_question.append(line)
    if current_question:
        questions.append(current_question)

    print("\n=== Delete Questions ===")
    for i, question in enumerate(questions, start=1):
        print(f"{i}. {question[0].strip()}")

    try:
        choice = int(input("\nEnter the number of the question to delete: ").strip())
        if 1 <= choice <= len(questions):
            del questions[choice - 1]

            with open(filename, 'w') as f:
                for question in questions:
                    f.writelines(question)

            print("\nQuestion deleted successfully!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def display_menu():
    """Display the main menu."""
    print("\n=== Quiz Creator Menu ===")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Edit Question")
    print("4. Delete Question")
    print("5. Exit")


def main():
    """Main function to run the quiz creator."""
    filename = "quiz_record.txt"

    print("Welcome to Quiz Creator!")
    print("Add questions to your quiz. Press Ctrl+C to finish.")

    try:
        while True:
            display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == '1':
                question = questions_getter()
                answers = choices()
                correct_answer_value = correct_answer(answers)
                quiz_question_saver(question, answers, correct_answer_value)
                print("\nQuestion added successfully!")
            elif choice == '2':
                if os.path.exists(filename) and os.path.getsize(filename) > 0:
                    with open(filename, 'r') as f:
                        print("\n=== Available Questions ===")
                        print(f.read())
                else:
                    print("\nNo questions available!")
            elif choice == '3':
                edit_questions(filename)
            elif choice == '4':
                delete_questions(filename)
            elif choice == '5':
                print("\nQuiz creation completed!")
                print(f"All questions have been saved to {filename}")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")

    except KeyboardInterrupt:
        print("\n\nQuiz creation completed!")
        print(f"All questions have been saved to {filename}")


if __name__ == "__main__":
    main()