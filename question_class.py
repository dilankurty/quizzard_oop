class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
        self.user_answer = None

    def is_correct(self, user_choice):
        self.user_answer = user_choice.upper()
        return self.user_answer == self.answer
        