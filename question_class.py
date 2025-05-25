class Question:
    def __init__(self, question_text, choices, answer):
        self.question_text = question_text
        self.choices = choices
        self.answer = answer.upper()
        self.user_answer = None

        