# Flask TO‑DO List App

A simple yet fully functional **Flask** application for managing tasks: add, mark complete, delete, and view tasks in a lightweight Todo interface.

---

## 🚀 Features

- ✅ Create new tasks
- 🔁 Mark tasks as complete/incomplete
- 🗑️ Remove tasks permanently
- 💾 Persistent storage using SQLite (`todo.db`)
- 🎨 Basic styling with external CSS
- 🧪 Form handling and validation using Flask
- 🔥 Flash messages for user feedback

---

## 📁 Project Structure

/to_do_app/
├── app.py
├── todo.db
├── static/
│ └── style.css
├── templates/
│ ├── base.html
│ ├── index.html
│ └── add_task.html # if separate view exists
└── README.md


---

## ▶️ Getting Started

### Prerequisites
- Python 3.7+
- Flask installed:  
  ```bash
  pip install Flask
Installation & Run
Clone the repo:

git clone https://github.com/RamGenAi22/TO-DO-LIST.git
cd TO-DO-LIST
Install dependencies:


pip install Flask
Run the app:


python app.py
Access it at http://127.0.0.1:5000/

🔍 How It Works
app.py defines the Flask app with routes to:

Show existing tasks

Add new tasks via forms

Toggle completion and delete

Tasks stored in SQLite database (todo.db)

Uses Flask’s request for form data and flash() for user messages

Templates extend a shared layout (base.html) for consistency

🎨 Styling
CSS in static/style.css

Automatically linked in templates using Flask's url_for('static', filename='style.css')

Simple, clean UI focusing on task readability and usability

✨ Future Enhancements
Add task editing (update functionality)

Use Flask‑WTF and SQLAlchemy for more robust form & database handling

Implement user authentication (login, register)

Add filter categories (by date/completion)

Build RESTful API endpoints for potential integration

🤝 Contributions
Welcome! You’re invited to contribute. Fork the repo, make changes, and open a pull request.
See CONTRIBUTING.md for more (if you include one).

📬 Author
RamGenAi22
Flask learner and aspiring AI engineer.
Enjoyed using this project? Feel free to ⭐ the repo!

🧪 License
This project is open-source and available under the MIT License.


