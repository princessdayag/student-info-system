Student Information System
Overview

The Student Information System is a simple Python program designed to manage student records.
It allows users to add, view, update, and delete student information. All student data is stored in a JSON file to ensure that records are saved even after the program is closed.

Features

Add new student information

View the list of all students

Search for a student by ID

Update existing student details

Delete student records

Save and load data using a JSON file

How to Run the Program
Step 1: Open the Project Folder

Make sure the project folder is opened in Visual Studio Code (VS Code) or any code editor you use.

Step 2: Navigate to the Project Directory

In the terminal, use the following command to move into the project folder:

cd student-info-system

Step 3: Run the Program

Once inside the project folder, run the following command to start the program:

python -m src.main

Project Structure
student-info-system/
│
├── data/
│   └── students.json
│
├── logs/
│   └── app.log
│
├── src/
│   ├── models/
│   │   └── student.py
│   ├── services/
│   │   └── student_services.py
│   └── main.py
│
└── README.md

Author

Developed by Princess Dayag