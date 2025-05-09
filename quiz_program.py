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
        
