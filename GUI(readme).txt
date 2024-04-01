# Student Name Tracker

## Overview
This is a Python GUI application built using Tkinter that allows users to track and manage student names. The application consists of a login window where users can log in or create a new account, and a student name window where users can add, edit, save, and delete student names.

## Features
### Login Window
- Users can enter their username and password to log in.
- Users can create a new account by providing their personal information (first name, last name, student name, parent phone number, email).

### Student Name Window
- After logging in, users are greeted with a welcome message indicating the current day of the week.
- Users can add multiple student names at once by separating them with commas.
- Each student name entered is displayed in a listbox.
- Users can select a student name from the list to edit it.
- Users can edit the selected student name and save the changes.
- Users can delete a selected student name.
- Users can toggle the shift status of a student name, indicating whether the student is in or out of the classroom (green color for "in" and red color for "out").
- The list of student names is saved to a file ("student_names.txt") for persistence across sessions.
- Users can view a list of saved student names.
- Users can quit the application.

## How to Use
1. Run the program.
2. Enter your username and password in the login window to log in.
3. If you don't have an account, click the "Create Account" button and provide the required information.
4. After logging in, enter the names of students in the class in the student name window.
5. Click the "Add" button to add multiple student names at once (separate names with commas).
6. Select a student name from the list to edit or delete it.
7. Edit the student name in the entry field and click the "Save" button to save the changes.
8. Click the "Toggle Shift" button to toggle the shift status of a student name.
9. Click the "Saved Lists" button to view a list of saved student names.
10. Click the "Quit" button to exit the application.

## Dependencies
- Python 3.12
- Tkinter (Python's standard GUI library)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
