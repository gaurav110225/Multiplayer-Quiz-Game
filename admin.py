import json
import os
from constants import QUESTIONS_FILE

def load_questions():
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_questions(questions):
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4)
    print("Questions saved successfully!")

def add_question():
    question = input("Enter the question text: ").strip()
    options = []
    print("Enter 4 options:")
    for i in range(1, 5):
        opt = input(f"Option {i}: ").strip()
        options.append(opt)
    
    while True:
        answer = input("Enter the number of the correct option (1-4): ").strip()
        if answer.isdigit() and 1 <= int(answer) <= 4:
            answer = int(answer)
            break
        print("Invalid input. Please enter a number between 1 and 4.")

    return {"question": question, "options": options, "answer": answer}

def main():
    print("=== Quiz Admin CLI ===")
    questions = load_questions()
    
    while True:
        print("\n1. Add a new question")
        print("2. View all questions")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            q = add_question()
            questions.append(q)
            save_questions(questions)
        elif choice == "2":
            if not questions:
                print("No questions available.")
            else:
                print("\nCurrent Questions:")
                for idx, q in enumerate(questions, start=1):
                    print(f"{idx}. {q['question']}")
                    for i, opt in enumerate(q["options"], start=1):
                        print(f"   {i} - {opt}")
                    print(f"   Correct option: {q['answer']}")
        elif choice == "3":
            print("Exiting Admin CLI.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
