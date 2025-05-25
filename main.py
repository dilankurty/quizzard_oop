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

def list_available_subjects():
    """Returns a list of quiz subjects based on available JSON files."""
    quiz_file_names = os.listdir()
    subject_files = [
        file_name for file_name in quiz_file_names if file_name.endswith("_quiz.json")
    ]
    subject_names = [
        file_name.replace("_quiz.json", "").capitalize() for file_name in subject_files
    ]
    return subject_names

def choose_subject(subject_list):
    """Allows the user to select a subject from a list."""
    print("\n📚 Available Quiz Subjects:")
    for subject_index, subject_name in enumerate(subject_list, start=1):
        print(f"{subject_index}. {subject_name}")

    while True:
        try:
            subject_choice = int(input("Select a subject number: "))
            if 1 <= subject_choice <= len(subject_list):
                return subject_list[subject_choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")