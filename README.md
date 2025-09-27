# 🏆 Multiplayer-Quiz-Game

This is a **Python-based offline multiplayer quiz game** using sockets. Multiple users can take quizzes simultaneously through the terminal. The game stores results in **JSON/Markdown files** and allows viewing leaderboards and graphs separately.

The project demonstrates **file management, threading, functions, modular design**, and is suitable for engineering students.

---

## 📂 Project Structure

```
Quiz-Game/
│── server.py          # Quiz server (socket-based)
│── client.py          # Quiz client (user takes the quiz)
│── view_results.py    # Viewer for leaderboard/results
│── admin.py           # Admin CLI to add questions
│── constants.py       # Constants for file paths, host, port
│── questions.json     # Stores quiz questions
│── results.json       # Stores quiz results
│── leaderboard.md     # Auto-generated leaderboard
│── README.md          # Project documentation
```

---

## ⚡ Features

* Multiple users can take quizzes simultaneously via terminal.
* Admin can **add questions interactively** using `admin.py`.
* Multiple-choice questions with **numbered options** (1, 2, 3, 4).
* Duplicate usernames are **not allowed**; scores are updated instead of adding duplicate entries.
* Leaderboard automatically generated in **Markdown**.
* Optionally view results as **text table** or **matplotlib graph**.

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd Quiz-Game
```

---

### 2️⃣ Create a Python Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### 1️⃣ Admin CLI — Add Questions

```bash
python admin.py
```

* Add new questions interactively:

  * Enter question text
  * Enter 4 options
  * Specify correct option number (1-4)
* View existing questions
* Questions are stored in `questions.json`

---

### 2️⃣ Start the Server

```bash
python server.py
```

* Server listens on `127.0.0.1:65432` (configurable in `constants.py`).
* Handles multiple clients simultaneously.

---

### 3️⃣ Start a Client (Take Quiz)

```bash
python client.py
```

* Enter your **name**.
* Answer questions one by one with **numbered options**.
* After completing the quiz, the score is **saved on the server**.

> Multiple users can run `client.py` in **separate terminals** at the same time.

---

### 4️⃣ View Leaderboard / Results

```bash
python view_results.py
```

Options:

1. **View Leaderboard** → Markdown table displayed in terminal.
2. **View Results Graph** → Bar chart showing scores using matplotlib.

---

## ⚙️ Files Explanation

* **`constants.py`** → Stores constants like `HOST`, `PORT`, and file paths.
* **`server.py`** → Handles quiz flow, multiple clients, result storage, and leaderboard update.
* **`client.py`** → User interface for taking the quiz.
* **`view_results.py`** → Displays leaderboard and results graph.
* **`admin.py`** → CLI tool for adding quiz questions interactively.
* **`questions.json`** → Stores quiz questions. Example:

```json
[
  {
    "question": "What is 2 + 2?",
    "options": ["1", "2", "3", "4"],
    "answer": 4
  }
]
```

* **`results.json`** → Stores user scores and total questions.
* **`leaderboard.md`** → Auto-generated leaderboard in Markdown format.

---

## 🔄 Project Flow

```
          ┌───────────────┐
          │   Admin       │
          │  (admin.py)   │
          │ Adds questions│
          └───────┬───────┘
                  │
          ┌───────▼───────┐
          │   Server      │
          │ (server.py)   │
          │ Handles quiz  │
          │ Saves results │
          └───────┬───────┘
 ┌───────────────┼───────────────┐
 │               │               │
▼               ▼               ▼
Client         Client          Client
(User1)       (User2)        (User3)
│               │               │
└───────┬───────┴───────┬───────┘
        ▼               ▼
  Results Viewer  (view_results.py)
  Text/Graph display
```
---
