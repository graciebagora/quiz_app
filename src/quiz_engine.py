"""Module 2: Quiz Engine & Data Processing"""
from src.models import Question, QuizResult

class QuizEngine:
    def __init__(self):
        self.questions = self._load_sample_questions()

    def _load_sample_questions(self) -> list:
        return [
            # Python Questions
            Question(1, "What is the output of print(type([]))?", ["<class 'tuple'>", "<class 'list'>", "<class 'dict'>", "<class 'set'>"], 2, "Python"),
            Question(2, "Which keyword is used to define a function in Python?", ["func", "def", "function", "lambda"], 2, "Python"),
            Question(3, "Which of the following is an immutable data type?", ["List", "Dictionary", "Set", "Tuple"], 4, "Python"),
            Question(4, "What operator is used for exponentiation (power)?", ["^", "**", "//", "%"], 2, "Python"),

            # Data Structures Questions
            Question(5, "What data structure uses LIFO (Last In First Out)?", ["Queue", "Array", "Stack", "Tree"], 3, "Data Structures"),
            Question(6, "What is the time complexity of Binary Search?", ["O(n)", "O(n^2)", "O(log n)", "O(1)"], 3, "Data Structures"),
            Question(7, "Which data structure follows FIFO (First In First Out)?", ["Stack", "Queue", "Binary Tree", "Graph"], 2, "Data Structures"),

            # General CS Questions
            Question(8, "Which component is known as the brain of the computer?", ["RAM", "CPU", "Hard Drive", "GPU"], 2, "General CS"),
            Question(9, "What does HTTP stand for?", ["HyperText Transfer Protocol", "HighText Transfer Process", "Hyperlink Text Test Protocol", "Home Tool Transfer Program"], 1, "General CS"),
            Question(10, "Which system component stores data permanently?", ["RAM", "Cache", "SSD / Hard Disk", "Registers"], 3, "General CS")
        ]

    def get_topics(self) -> list:
        return list(set(q.topic for q in self.questions))

    def run_quiz(self, username: str, topic: str) -> QuizResult:
        topic_questions = [q for q in self.questions if q.topic.lower() == topic.lower()]
        if not topic_questions:
            print("No questions found for this topic.")
            return QuizResult(username, topic, 0, 0)

        score = 0
        print(f"\n--- Starting Quiz: {topic} ---")
        for idx, q in enumerate(topic_questions, 1):
            print(f"\nQ{idx}: {q.text}")
            for opt_idx, opt in enumerate(q.options, 1):
                print(f"  {opt_idx}. {opt}")

            while True:
                try:
                    choice = int(input("Your choice (1-4): "))
                    if 1 <= choice <= len(q.options):
                        break
                    print("Please enter a valid option number (1-4).")
                except ValueError:
                    print("Invalid input! Please enter a number.")

            if q.is_correct(choice):
                print(" Correct!")
                score += 1
            else:
                print(f" Wrong! Correct answer was option {q.correct_option}.")

        return QuizResult(username, topic, score, len(topic_questions))