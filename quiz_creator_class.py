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
