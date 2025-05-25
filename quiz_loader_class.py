import os
import json
from question_class import Question

class QuizLoader:
    """
    Loads quiz data from a specific subject JSON file and converts them into Question objects.
    """

    @staticmethod
    def load_questions(subject_name):
        """
        Loads and returns a list of Question objects for the given subject.
        Expects a file named '{subject_name}_quiz.json'.
        """
        filename = f"{subject_name.lower()}_quiz.json"

        if not os.path.exists(filename):
            print(f"\nNo quiz file found for subject: {subject_name}")
            return []