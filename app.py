import os
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

app = Flask(__name__)

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

@app.route("/", methods=["GET", "POST"])
def index():
    cursor = conn.cursor()

    if request.method == "POST":
        task = request.form["task"]
        status = request.form["status"]
        created_at = request.form["created_at"]

        query = "INSERT INTO tasks (task, status, date) VALUES (%s, %s, %s)"
        cursor.execute(query, (task, status, created_at))
        conn.commit()

    cursor.execute("SELECT * FROM tasks ORDER BY date DESC")
    tasks = cursor.fetchall()
    cursor.close()

    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)