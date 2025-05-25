from quiz_creator import QuizCreator
from quiz_loader import QuizLoader
from quiz_class import Quiz

import os

def clear_terminal():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def show_main_menu():
    """Displays the main menu and returns the user's choice."""
    print("\nWelcome to Quizzard!")
    print("1. Take a Quiz")
    print("2. Create a Quiz")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid input. Please enter 1, 2, or 3.")