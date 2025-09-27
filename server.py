import socket
import threading
import json
import sys
import os
from constants import HOST, PORT, QUESTIONS_FILE, RESULTS_FILE, LEADERBOARD_FILE


# Utility functions
def load_json(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# Save JSON data to file
def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# Update leaderboard markdown file
def update_leaderboard(results):
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        f.write("# Quiz Leaderboard\n\n")
        f.write("| Rank | Name | Score |\n")
        f.write("|------|------|-------|\n")
        for i, r in enumerate(sorted_results, start=1):
            f.write(f"| {i} | {r['name']} | {r['score']}/{r['total']} |\n")
    return sorted_results


# Handle client connection
def handle_client(conn, addr):
    print(f"Connected by {addr}")

    try:
        # Get user name
        conn.sendall("Enter your name: ".encode())
        name = conn.recv(1024).decode().strip()
        if not name:
            conn.close()
            return

        # Load questions
        questions = load_json(QUESTIONS_FILE)
        if not questions:
            conn.sendall("No questions available.\n".encode())
            conn.close()
            return

        score = 0
        total = len(questions)

        for q in questions:
            # Send question and options
            question_text = f"\n{q['question']}\n"
            for idx, opt in enumerate(q["options"], start=1):
                question_text += f"{idx} - {opt}\n"
            question_text += "Your answer (1-4): "
            conn.sendall(question_text.encode())

            # Receive answer
            ans = conn.recv(1024).decode().strip()
            if ans.isdigit() and int(ans) == q["answer"]:
                score += 1

        # Save results
        results = load_json(RESULTS_FILE)
        found = False
        for r in results:
            if r["name"].lower() == name.lower():
                r["score"] = score
                r["total"] = total
                found = True
                break
        if not found:
            results.append({"name": name, "score": score, "total": total})

        save_json(RESULTS_FILE, results)
        update_leaderboard(results)

        conn.sendall(f"\nQuiz submitted successfully! Your score: {score}/{total}\n".encode())

    finally:
        conn.close()


# Main server loop
def main():
    # Create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        s.settimeout(1)
        print(f"Server started on {HOST}:{PORT}")

        # Accept clients
        try:
            while True:
                try:
                    conn, addr = s.accept()
                    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
                except socket.timeout:
                    continue
        except KeyboardInterrupt:
            print("\nShutting down server gracefully...")
        finally:
            s.close()
            sys.exit(0)


if __name__ == "__main__":
    main()
