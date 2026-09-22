"""Module 1: User Management & Data Storage[cite: 1]"""
import json
import os

class UserManager:
    def __init__(self, filepath="results.json"):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump([], f)

    def save_result(self, quiz_result):
        data = self.load_all_results()
        data.append(quiz_result.to_dict())
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)

    def load_all_results(self) -> list:
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []