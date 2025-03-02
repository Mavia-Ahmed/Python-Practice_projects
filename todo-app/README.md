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


### 🎨 CSS Styling (static/style.css)
```
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 20px;
}
.task-list {
    list-style: none;
    padding: 0;
}
.task {
    padding: 10px;
    margin: 5px;
    background: lightgray;
    display: flex;
    justify-content: space-between;
}
button {
    background: red;
    color: white;
    border: none;
    padding: 5px;
    cursor: pointer;
}
```


### 🖥️ Frontend (templates/index.html)
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>📝 To-Do List</h1>
    <form action="/add" method="POST">
        <input type="text" name="task" placeholder="Enter task" required>
        <input type="time" name="time" required>
        <button type="submit">Add Task</button>
    </form>

    <ul class="task-list">
        {% for task in tasks %}
        <li class="task">
            {{ task[1] }} - {{ task[2] }} 
            <a href="/delete/{{ task[0] }}"><button>Delete</button></a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```




