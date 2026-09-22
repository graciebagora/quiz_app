"""Main Program Entry Point."""
from src.user_manager import UserManager
from src.quiz_engine import QuizEngine
from src.analytics import AnalyticsManager

def main():
    user_mgr = UserManager()
    engine = QuizEngine()
    analytics = AnalyticsManager(user_mgr)

    print("====================================")
    print(" Welcome to the Quiz Application ")
    print("====================================")
    username = input("Enter your username: ").strip()

    while not username:
        username = input("Username cannot be empty. Try again: ").strip()

    while True:
        print("\n--- Main Menu ---")
        print("1. Take a Quiz")
        print("2. View Performance Report")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            topics = engine.get_topics()
            print("\nAvailable Topics:")
            for idx, topic in enumerate(topics, 1):
                print(f"{idx}. {topic}")

            try:
                t_choice = int(input("Select topic number: "))
                if 1 <= t_choice <= len(topics):
                    selected_topic = topics[t_choice - 1]
                    result = engine.run_quiz(username, selected_topic)
                    user_mgr.save_result(result)
                    print(f"\nQuiz complete! Score: {result.score}/{result.total}")
                else:
                    print("Invalid topic selection.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "2":
            analytics.display_user_report(username)

        elif choice == "3":
            print(f"\nGoodbye, {username}!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()