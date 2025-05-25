from quiz_creator import QuizCreator
from quiz_loader import QuizLoader
from quiz_class import Quiz

import os

def clear_terminal():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

