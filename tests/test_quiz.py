import unittest
from src.models import Question, QuizResult

class TestQuizModels(unittest.TestCase):
    def test_question_correct_answer(self):
        q = Question(1, "What is 2+2?", ["3", "4", "5", "6"], 2, "Math")
        self.assertTrue(q.is_correct(2))
        self.assertFalse(q.is_correct(1))

    def test_quiz_result_percentage(self):
        result = QuizResult("testuser", "Math", 4, 5)
        self.assertEqual(result.percentage, 80.0)

if __name__ == "__main__":
    unittest.main()