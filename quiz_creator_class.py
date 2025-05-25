import json
import os

class QuizCreator:
    def __init__(self):
        self.subject = ""
        self.filename = ""

    def choose_subject(self):
        """Prompt user to choose a subject or create a new one."""
        print("\nChoose a subject for the quiz:")
        existing_files = [f.replace('_quiz.json', '').capitalize() 
                          for f in os.listdir() if f.endswith('_quiz.json')]

        if existing_files:
            for index, subject_name in enumerate(existing_files, 1):
                print(f"{index}. {subject_name}")
        else:
            print("No subjects available yet.")

        print("0. Create a new subject")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    self.subject = input("Enter new subject name: ").strip().capitalize()
                elif 1 <= choice <= len(existing_files):
                    self.subject = existing_files[choice - 1]
                else:
                    print("Invalid choice. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        self.filename = f"{self.subject.lower()}_quiz.json"

    def create_question(self):
        """Ask the user for a new question and write it to the quiz file."""
        print(f"\nCreating a question for {self.subject}")

        question_text = input("Enter the question: ").strip()
        choices = {}

        for letter in ['A', 'B', 'C', 'D']:
            while True:
                choice = input(f"Enter choice {letter}: ").strip()
                if choice:
                    choices[letter] = choice
                    break
                else:
                    print("Choice cannot be empty.")

        while True:
            correct_answer = input("Enter the correct answer (A/B/C/D): ").upper()
            if correct_answer in choices:
                break
            else:
                print("Invalid answer. Must be one of A, B, C, or D.")

        question_entry = {
            "question": question_text,
            "choices": choices,
            "answer": correct_answer
        }

        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
        else:
            data = []

        data.append(question_entry)

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

        print("✅ Question added successfully.")

    def create(self):
        """Main entry point to handle the full creation flow."""
        self.choose_subject()

        while True:
            self.create_question()

            while True:
                next_action = input("\nWhat would you like to do next?\n"
                                    "[1] Add another question\n"
                                    "[2] Select another subject\n"
                                    "[3] Return to main menu\n"
                                    "Enter choice: ")
                if next_action == "1":
                    break
                elif next_action == "2":
                    self.choose_subject()
                    break
                elif next_action == "3":
                    return
                else:
                    print("Invalid input. Please select 1, 2, or 3.")