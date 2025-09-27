import json
import matplotlib.pyplot as plt
from constants import LEADERBOARD_FILE, RESULTS_FILE


# View Leaderboard
def view_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Leaderboard not found. Run a quiz first.")


# View Results Graph
def view_results_graph():
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            results = json.load(f)
    except FileNotFoundError:
        print("No results found.")
        return

    names = [r["name"] for r in results]
    scores = [r["score"] for r in results]

    plt.bar(names, scores, color="skyblue")
    plt.xlabel("Players")
    plt.ylabel("Scores")
    plt.title("Quiz Results")
    plt.show()


if __name__ == "__main__":
    print("1. View Leaderboard")
    print("2. View Results Graph")
    choice = input("Enter choice: ")

    if choice == "1":
        view_leaderboard()
    elif choice == "2":
        view_results_graph()
    else:
        print("Invalid choice")
