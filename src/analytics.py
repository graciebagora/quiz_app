"""Module 3: Reporting & Score Analytics[cite: 1]"""

class AnalyticsManager:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def display_user_report(self, username: str):
        results = self.user_manager.load_all_results()
        user_results = [r for r in results if r["username"].lower() == username.lower()]

        if not user_results:
            print(f"\nNo history found for user '{username}'.")
            return

        print(f"\n=== Performance Report for {username} ===")
        total_quizzes = len(user_results)
        avg_score = sum(r["percentage"] for r in user_results) / total_quizzes

        for r in user_results:
            print(f"Topic: {r['topic']} | Score: {r['score']}/{r['total']} ({r['percentage']:.1f}%)")

        print("-----------------------------------")
        print(f"Total Quizzes Taken: {total_quizzes}")
        print(f"Average Percentage: {avg_score:.2f}%\n")