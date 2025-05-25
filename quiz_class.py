class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self, user_name):
        import random
        random.shuffle(self.questions)
        print(f"\nWelcome to Quizzard, {user_name}! Let's begin your quiz.")

        for index, question in enumerate(self.questions, 1):
            print(f"\nQuestion {index}: {question.text}")
            for option, value in question.choices.items():
                print(f"{option}. {value}")

            while True:
                user_answer = input("Your answer (A/B/C/D): ").strip().upper()
                if user_answer in question.choices:
                    break
                else:
                    print("Invalid input. Please choose A, B, C, or D.")

            
            if question.is_correct(user_answer):
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer was: {question.answer}")

        print(f"\nQuiz finished! Your score: {self.score}/{len(self.questions)}")

        self.review()

    def review(self):
        print("\n📋 Review of Your Answers:")
        for index, question in enumerate(self.questions, 1):
            correct = question.user_answer == question.answer
            status = "✅ Correct" if correct else f"❌ Incorrect (Correct: {question.answer})"
            print(f"{index}. {question.text}")
            print(f"   Your Answer: {question.user_answer} — {status}")

