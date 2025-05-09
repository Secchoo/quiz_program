import os
import random
from colorama import Fore, Style, init
import sys


def clear_screen():
    """Clear the console screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_header():
    """Display the header of the quiz program."""
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "\n" + "=" * 40)
    print(Fore.CYAN + Style.BRIGHT + "            QUIZ TIME            ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.YELLOW + Style.BRIGHT + "\n🌟 Test Your Knowledge! 🌟\n")


def get_questions_from_file(file_path):
    """Load questions from the file"""
    questions = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            current_question = {}
            collecting_options = False

            for line in file:
                line = line.strip()
                if line.startswith("Question: "):
                    current_question = {
                        'text': line[10:],
                        'options': [],
                        'correct': None
                    }
                    collecting_options = True
                elif line.startswith(('a. ', 'b. ', 'c. ', 'd. ')) and collecting_options:
                    current_question['options'].append(line[3:])
                elif line.startswith("Correct answer: "):
                    correct_letter = line[16:].lower()
                    current_question['correct'] = current_question['options'][
                        ord(correct_letter) - ord('a')]
                    questions.append(current_question)
                    collecting_options = False

    except FileNotFoundError:
        print(Fore.RED + "\n🚨 Error: Quiz file not found!")
        sys.exit(1)

    return questions 
        

def present_question(question, question_number, total_questions):
    """Display a single question with formatted output."""
    print(Fore.MAGENTA + Style.BRIGHT + 
          f"\n📝 Question {question_number}/{total_questions}")
    print(Fore.WHITE + Style.BRIGHT + f"\n{question['text']}\n")
    
    options = question['options'].copy()
    random.shuffle(options)
    
    for index, option in enumerate(options):
        print(Fore.CYAN + Style.BRIGHT + f"   {chr(65 + index)}) {option}")
    
    return options


def get_user_choice():
    """Get and validate user's answer choice."""
    while True:
        choice = input(Fore.GREEN + Style.BRIGHT + 
                       "\n✏️  Your answer (A-D): ").upper()
        if choice in {'A', 'B', 'C', 'D'}:
            return choice
        print(Fore.RED + Style.BRIGHT + "⚠️  Invalid choice! Please enter A, B, C, or D")


def calculate_score(selected_option, correct_answer):
    """Check if answer is correct and return points."""
    if selected_option == correct_answer:
        print(Fore.GREEN + Style.BRIGHT + "\n✅ Correct! +1 Point! ✅")
        return 1
    print(Fore.RED + Style.BRIGHT + 
          f"\n❌ Incorrect! Correct answer: {correct_answer} ❌")
    return 0


def show_final_results(score, total):
    """Display final score with visual feedback."""
    display_header()
    percentage = (score / total) * 100
    print(Fore.YELLOW + Style.BRIGHT + "\n🎉 Quiz Complete! Final Results 🎉")
    print(Fore.CYAN + Style.BRIGHT + 
          f"\n📊 Your Score: {score}/{total} ({percentage:.1f}%)")
    
    if percentage >= 90:
        print(Fore.GREEN + Style.BRIGHT + "\n🌈 Perfect Score! You're a genius! 🧠")
    elif percentage >= 75:
        print(Fore.GREEN + Style.BRIGHT + "\n🌟 Excellent Work! Keep it up! 💪")
    elif percentage >= 50:
        print(Fore.YELLOW + Style.BRIGHT + "\n👍 Good Effort! Keep practicing! 📚")
    else:
        print(Fore.RED + Style.BRIGHT + "\n💪 Never Give Up! Try again! 🔁")