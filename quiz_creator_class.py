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
