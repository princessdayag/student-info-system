# Student Information System

## Overview
The Student Information System is a Python-based application developed to manage student records efficiently. It allows users to add, view, update, search, and delete student information. All data is stored in a JSON file to ensure records are saved even after the program is closed.

This project was created as part of a laboratory exam to demonstrate the use of:
- Python programming fundamentals
- File handling (JSON)
- Functions and modular coding
- Organized project structure
- Version control using Git and GitHub

---

## Features
- Add Student Information — Create new student records with essential details.
- View All Students — Display all stored student records.
- Search Student by ID — Quickly find a specific student record.
- Update Student Details — Edit or modify existing student information.
- Delete Student Records — Remove a student’s data from the system.
- Data Persistence — All records are saved and loaded automatically using a JSON file.

---

## Project Structure
student-info-system/
│
├── config/
│ └── config.json
│
├── data/
│ └── students.json
│
├── logs/
│ └── app.log
│
├── src/
│ ├── models/
│ │ └── student.py
│ ├── services/
│ │ └── student_services.py
│ ├── utils/
│ │ └── init.py
│ └── main.py
│
├── tests/
│ └── init.py
│
├── .gitignore
├── requirements.txt
└── README.md

How to Run the Program

Step 1: Open the Project Folder
Open the entire project folder (student-info-system) in Visual Studio Code (VS Code) or any preferred code editor.

Step 2: Open the Terminal
Open a terminal inside VS Code and navigate to the project directory:

cd student-info-system

Step 3: Run the Program
Execute the program by running:
python -m src.main
Step 4: Interact with the System
Once running, you can choose from the menu options to:
- Add new students
- View student lists
- Search by student ID
- Update or delete existing records

All changes will automatically be stored in the students.json file.

---

Requirements
To ensure the program runs smoothly, install dependencies listed in the requirements.txt file.

Install requirements:
pip install -r requirements.txt
Included Package:
- jsonschema — for handling JSON validation and structure.

---

Testing
Basic structure for testing is included in the tests/ directory. You can extend this folder to include unit tests for each feature (optional for lab submission).

---

Additional Folders
- config/ → Contains configuration files for setup.
- data/ → Stores student records in JSON format.
- logs/ → Intended for future logging features.
- src/utils/ → Contains utility or helper files.

---

## Author
Developed by: Princess Dayag