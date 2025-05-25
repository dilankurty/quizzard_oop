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
        
        try:
            with open(filename, "r", encoding="utf-8") as quiz_file:
                data = json.load(quiz_file)

                questions = []
                for entry in data:
                    # Basic validation
                    if "question" in entry and "choices" in entry and "answer" in entry:
                        question = Question(
                            text=entry["question"],
                            choices=entry["choices"],
                            answer=entry["answer"]
                        )
                        questions.append(question)
                    else:
                        print("⚠️ Skipping invalid question format.")

                return questions

        except json.JSONDecodeError:
            print("❌ Error: The quiz file is not a valid JSON.")
            return []
        except Exception as error:
            print(f"Unexpected error while loading quiz: {error}")
            return []
