# Student Tracker

## Overview
This is a simple Python GUI application built using Tkinter that allows users to track and manage students attendance in a classroom. The application consists of two windows: a login window and a student name window.

## Features
### Login Window
- Users can enter their username and password to log in (authentication is not implemented in this demo).
- Upon successful login, the student name window is displayed.
- Users can create a new account by clicking the "Create Account" button, which opens a new window for entering account information.

### Student Name Window
- After logging in, users are greeted with a welcome message indicating the current day of the week.
- Users can enter the names of students in a class.
- Users can add multiple student names at once by separating them with commas.
- Each student name entered is displayed in a listbox.
- Users can select a student name from the list to edit it.
- Users can edit the selected student name and save the changes.
- Users can delete a selected student name from the list.
- The list of student names is saved to a file ("student_names.txt") for persistence across sessions.
- Users can view a list of saved student names.
- Users can quit the application.

## How to Use
1. Run the program.
2. Enter your username and password in the login window (authentication is not implemented in this demo).
3. After logging in, enter the names of students in the class in the student name window.
4. Click the "Add" button to add multiple student names at once (separate names with commas).
5. Select a student name from the list to edit or delete it.
6. Edit the student name in the entry field and click the "Save" button to save the changes.
7. Click the "Delete" button to delete the selected student name from the list.
8. Click the "Saved Lists" button to view a list of saved student names.
9. Click the "Quit" button to exit the application.

## Dependencies
- Python 3.11.5
- Tkinter (Python's standard GUI library)

## License
This project is licensed under the MIT License - see the LICENSE file for details.







