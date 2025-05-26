from quiz_creator_class import QuizCreator
from quiz_loader_class import QuizLoader
from quiz_class import Quiz
from leaderboard_class import Leaderboard

import os

def clear_terminal():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def show_main_menu():
    """Displays the main menu and returns the user's choice."""
    print("📋 MENU:")
    print("[1] Create a Quiz")
    print("[2] Take a Quiz")
    print("[3] View Leaderboard")
    print("[4] Exit")

    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")

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

def take_quiz():
    """Handles the quiz-taking flow."""
    available_subjects = list_available_subjects()
    if not available_subjects:
        print("⚠️ No quiz subjects found. Please create a quiz first.")
        return

    selected_subject = choose_subject(available_subjects)
    loaded_questions = QuizLoader.load_questions(selected_subject)

    if not loaded_questions:
        print("⚠️ No valid questions found in this quiz.")
        return

    user_name = input("Enter your name: ").strip()
    quiz_instance = Quiz(loaded_questions, selected_subject)
    quiz_instance.start(user_name)

def main():
    """Main control loop for Quizzard."""
    while True:
        clear_terminal()
        selected_option = show_main_menu()

        if selected_option == "1":
            quiz_creator = QuizCreator()
            quiz_creator.create()
        elif selected_option == "2":
            take_quiz()
        elif selected_option == "3":
            Leaderboard.display()
        elif selected_option == "4":
            print("👋 Goodbye! Thanks for using Quizard.")
            break

        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()