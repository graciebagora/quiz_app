"""Data models for Questions and Quiz Results."""

class Question:
    def __init__(self, q_id: int, text: str, options: list, correct_option: int, topic: str):
        self.q_id = q_id
        self.text = text
        self.options = options
        self.correct_option = correct_option  # 1-indexed (1, 2, 3, or 4)
        self.topic = topic

    def is_correct(self, user_choice: int) -> bool:
        return user_choice == self.correct_option


class QuizResult:
    def __init__(self, username: str, topic: str, score: int, total: int):
        self.username = username
        self.topic = topic
        self.score = score
        self.total = total
        self.percentage = (score / total) * 100 if total > 0 else 0.0

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "topic": self.topic,
            "score": self.score,
            "total": self.total,
            "percentage": self.percentage
        }