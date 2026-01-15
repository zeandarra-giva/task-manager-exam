# Task Management CLI Application

## Overview
A command-line tool to manage daily tasks, supporting Add, List, Update, Delete, and Complete operations.

## Prerequisites
* Python 3.x
* Database (MySQL or MongoDB)

## Setup Instructions
1. Clone the repository:
   `git clone <your-repo-link>`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Database Configuration:
   * **MySQL:** Run the script located in `schema/db_setup.sql` to create the database and tables.
   * **MongoDB:** Ensure your local MongoDB instance is running.
   * Update `src/db_connection.py` with your specific credentials.

## Usage
Run the application from the root directory:
`python src/main.py`

## Features
* **Modular Design:** Separation of concerns between database, logic, and UI.
* **Custom Algorithms:** Custom sorting and filtering logic (no built-in Python filters used).
* **Persistence:** Tasks are saved to the database and reloaded upon restart.
