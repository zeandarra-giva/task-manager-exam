# Python CLI Task Manager

## Overview of the Exam Task
The task is to create a simple CLI to-doo list app that create, view, update, and delete (CRUD) tasks using OOP principles and database of our choosing to store user data even after exiting the app.

## Setup Instructions

Follow these steps to set up and run the application locally.

### 1. Prerequisites
Ensure you that the following softwares were installed:
* **Python 3.x**: [Download Here](https://www.python.org/downloads/)
* **MySQL Server**: [Download Here](https://dev.mysql.com/downloads/mysql/)

### 2. Clone the Repository
Open terminal and run:
```bash
git clone [https://github.com/YOUR_USERNAME/task-manager-exam.git](https://github.com/YOUR_USERNAME/task-manager-exam.git)
cd task-manager-exam
```

### 3. Clone the Repository
#### Mac
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Setup Database
1. Login to MySQL
```bash
mysql -u root -p
```
2. Run this command
```bash
source schema/db_setup.sql;
```

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
