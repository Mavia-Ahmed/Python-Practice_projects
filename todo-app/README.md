# 📝 To-Do List App with Time Scheduling
A simple Flask-based To-Do List App where users can add tasks along with a scheduled time. This app stores tasks in an SQLite database and allows users to view and manage their tasks efficiently.


## 🚀 Features

✅ Add tasks with a specific time

✅ View all tasks in a structured list

✅ Delete tasks when completed

✅ Uses Flask (Python) and SQLite for storage

✅ Simple and user-friendly UI


## 🖥️ Installation & Setup
Follow these steps to set up and run the project:
1️⃣ Clone the Repository
```
git clone https://github.com/yourusername/todo-list-app.git
cd todo-list-app
```
2️⃣ Install Dependencies
Make sure you have Python 3 installed, then install Flask:
```
3️⃣ Run the App
```
python app.py
```
After running, open http://127.0.0.1:5000/ in your browser.
```


## 📂 Project Structure
```
📂 todo-list-app/
 ├── app.py          # Main Flask app
 ├── templates/
 │   ├── index.html  # HTML frontend
 │   ├── add_task.html  # Task input page
 ├── static/
 │   ├── style.css   # CSS styles
 ├── todo.db         # SQLite database (auto-generated)
 ├── README.md       # Project documentation
 ```


## 📝 Code Snippets
### 📌 app.py (Flask Backend)
```
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database if not exists
def create_table():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, time TEXT)")
    conn.commit()
    conn.close()

create_table()

@app.route("/")
def index():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]
    time = request.form["time"]  # Getting time input
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, time) VALUES (?, ?)", (task, time))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_task(id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
```



