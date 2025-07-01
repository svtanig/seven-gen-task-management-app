# Task Management Application (CLI-based with MongoDB)

A command-line task manager built with Python demonstrating:
- OOP principles
- Manual DB operations 
- CLI input validation
- Concurrency using threads

---

## 🔧 Setup Instructions

### 1. Clone Repository

git clone https://github.com/svtanig/seven-gen-task-management-app.git

cd seven-gen-task-management-app

### 2. Create Virtual Environment

python3 -m venv venv

source venv/bin/activate  # on Windows use venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Setup .env
Create a .env file in the root directory:

- MONGO_URI=mongodb://localhost:27017/
- DB_NAME=taskdb

Note: Ensure MongoDB is running locally.

### Run the App
- Standard CLI

python main.py

- Concurrent CLI (Multithreaded)

python cli_concurrent.py
