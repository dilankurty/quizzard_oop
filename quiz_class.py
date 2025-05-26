from leaderboard_class import Leaderboard
import random

class Quiz:
    def __init__(self, questions, subject):
        self.questions = questions
        self.subject = subject
        self.score = 0

    def start(self, user_name):
        random.shuffle(self.questions)
        total_questions = len(self.questions)

        for index, question in enumerate(self.questions, 1):
            print(f"\nQuestion {index}: {question.text}")
            for choice_letter, choice_text in question.choices.items():
                print(f"{choice_letter}. {choice_text}")

            while True:
                user_input = input("Your answer (A, B, C, D): ").strip().upper()
                if user_input in question.choices:
                    question.user_answer = user_input
                    break
                else:
                    print("Invalid input. Please choose A, B, C, or D.")

            if question.user_answer == question.answer:
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Incorrect. The correct answer was {question.answer}\n")

        self._show_results(user_name, total_questions)

        # Save to leaderboard
        Leaderboard.save_score(
            subject_name=self.subject,
            user_name=user_name,
            score=self.score,
            total=total_questions,
            percentage=(self.score / total_questions) * 100
        )

    def _show_results(self, user_name, total_questions):
        percentage = (self.score / total_questions) * 100
        print("──────────────────────────────")
        print(f"🎓 {user_name}, you scored {self.score}/{total_questions} ({percentage:.2f}%)")
        if percentage >= 90:
            print("🏆 Excellent work!")
        elif percentage >= 70:
            print("👏 Good job!")
        elif percentage >= 50:
            print("👍 Not bad, keep practicing!")
        else:
            print("📚 Keep learning! You'll do better next time.")
        print("──────────────────────────────")

