# Python CLI Task Manager

## Overview of the Exam Task
The task is to create a simple CLI to-doo list app that create, view, update, and delete (CRUD) tasks using OOP principles and database of our choosing to store user data even after exiting the app.

## Tech Stack

* **Language:** Python 3.x
* **Database:** MySQL
* **Driver:** `pymysql` (for raw SQL execution)
* **Architecture:** Modular design separating Database Logic, Business Logic, and User Interface.

## Project Structure

The project follows a modular architecture to ensure code maintainability:

```text
task-manager-exam/
├── src/
│   ├── main.py            # Entry point (User Interface & Menu Loop)
│   ├── task_manager.py    # Business Logic (CRUD operations)
│   ├── task.py            # Data Model (Task Class)
│   └── db_connection.py   # Database connection handling
├── schema/
│   └── db_setup.sql       # SQL script to initialize the database
├── .gitignore             # Files to ignore (venv, __pycache__)
└── README.md              # Documentation
