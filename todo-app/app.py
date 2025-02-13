from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY, 
                        task TEXT, 
                        time TEXT)''')  # Added time column
    conn.commit()
    conn.close()

init_db()

# Home Page - Show Tasks
@app.route("/")
def index():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

# Add Task with Time
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    time = request.form.get("time")  # Get selected time
    if task and time:
        conn = sqlite3.connect("todo.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task, time) VALUES (?, ?)", (task, time))
        conn.commit()
        conn.close()
    return redirect("/")

# Delete Task
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
