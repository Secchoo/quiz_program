import os
import random
from colorama import Fore, Style, init
import sys


def clear_screen():
    """Clear the console screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_header():
    """Display the header of the quiz program."""
    print(Fore.CYAN + Style.BRIGHT + "==============================")
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Quiz Program!" + Style.RESET_ALL)
    print(Fore.CYAN + "==============================" + Style.RESET_ALL)
    print(Fore.YELLOW + "Answer the questions to the best of your ability." + Style.RESET_ALL)