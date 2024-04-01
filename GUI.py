# Front end application 

# Author: Miled kalbourji

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Define the LoginWindow class, which represents the login window of the application
class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")  # Set the title of the window
        self.configure(bg="blue")  # Set background color to blue 
        
        # Variables to store username and password entered by the user
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Frame and widgets for entering username
        self.username_frame = tk.Frame(self)
        self.username_frame.pack(padx=20, pady=5)
        self.username_label = tk.Label(self.username_frame, text='Username')
        self.username_label.pack(side=tk.LEFT)
        self.username_entry = tk.Entry(self.username_frame, textvariable=self.username)
        self.username_entry.pack(side=tk.LEFT)
        
        # Frame and widgets for entering password
        self.password_frame = tk.Frame(self)
        self.password_frame.pack(padx=20, pady=5)
        self.password_label = tk.Label(self.password_frame, text='Password')
        self.password_label.pack(side=tk.LEFT)
        self.password_entry = tk.Entry(self.password_frame, textvariable=self.password, show='*')
        self.password_entry.pack(side=tk.LEFT)
        
        # Button for logging in
        self.login_button = tk.Button(self, text='Login', command=self.login)
        self.login_button.pack(pady=5)

        # Button for creating a new account
        self.create_account_button = tk.Button(self, text='Create Account', command=self.create_account_window)
        self.create_account_button.pack(pady=5)

    # Method to handle the login button click event
    def login(self):
        username = self.username.get()  # Get the username entered by the user
        password = self.password.get()  # Get the password entered by the user
        # You can perform login authentication here
        print("Username:", username)
        print("Password:", password)
        
        # Get current day of the week
        now = datetime.now()
        day_of_week = now.strftime("%A")
        
        # Open student name window after successful login
        self.withdraw()  # Hide login window
        student_name_window = StudentNameWindow(self, day_of_week)  # Create student name window
        student_name_window.wait_window()

    # Method to handle the create account button click event
    def create_account_window(self):
        create_account_window = CreateAccountWindow(self)  # Create the create account window
        create_account_window.wait_window()

# Define the CreateAccountWindow class, which represents the window for creating a new account
class CreateAccountWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Create Account")  # Set the title of the window
        self.parent = parent
        self.geometry("300x200")  # Set the size of the window

        # Labels and entry fields for account creation
        tk.Label(self, text="First Name:").pack()
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.pack()

        tk.Label(self, text="Last Name:").pack()
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.pack()

        tk.Label(self, text="Student Name:").pack()
        self.student_name_entry = tk.Entry(self)
        self.student_name_entry.pack()

        tk.Label(self, text="Parent Phone Number:").pack()
        self.parent_phone_entry = tk.Entry(self)
        self.parent_phone_entry.pack()

        tk.Label(self, text="Email:").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Button(self, text="Submit", command=self.submit_account).pack()  # Button to submit the account information

    # Method to handle the submit button click event
    def submit_account(self):
        # Get account information from entry fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        student_name = self.student_name_entry.get()
        parent_phone = self.parent_phone_entry.get()
        email = self.email_entry.get()

        # Process account creation (store information, etc.)
        print("Account Information:")
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Student Name:", student_name)
        print("Parent Phone Number:", parent_phone)
        print("Email:", email)

        # Close the window
        self.destroy()

# Define the StudentNameWindow class, which represents the window for managing student names
class StudentNameWindow(tk.Toplevel):
    def __init__(self, parent, day_of_week):
        super().__init__(parent)
        self.title("Student Name")  # Set the title of the window
        self.parent = parent
        self.configure(bg="red")  # Set background color to red 

        # Set window size
        self.geometry("400x300")

        # Welcome message label
        self.welcome_label = tk.Label(self, text=f"Welcome! Today is {day_of_week}!", font=("Arial", 14, "bold"))
        self.welcome_label.pack(pady=10)

        self.student_names = []  # List to store student names
        self.load_student_names()  # Load saved student names

        # Frame and widgets for adding student names
        self.student_frame = tk.Frame(self)
        self.student_frame.pack(pady=5)
        self.student_label = tk.Label(self.student_frame, text='Student Name', fg='gray')
        self.student_label.pack(side=tk.LEFT)
        self.student_entry = tk.Entry(self.student_frame)
        self.student_entry.pack(side=tk.LEFT, padx=5)
        self.student_entry.focus()
        self.add_button = tk.Button(self.student_frame, text='Add', command=self.add_students)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Label and listbox for displaying student names
        self.student_list_label = tk.Label(self, text='Student Names:')
        self.student_list_label.pack()
        self.student_listbox = tk.Listbox(self)
        self.student_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Button for toggling shift status of student names
        self.toggle_shift_button = tk.Button(self, text='Toggle Shift', command=self.toggle_shift_action)
        self.toggle_shift_button.pack()

        # Buttons for editing, saving, and deleting student names
        self.edit_button = tk.Button(self, text='Edit', command=self.edit_student)
        self.edit_button.pack(side=tk.LEFT, padx=5)
        self.save_button = tk.Button(self, text='Save', command=self.save_student)
        self.save_button.pack(side=tk.LEFT, padx=5)
        self.delete_button = tk.Button(self, text='Delete', command=self.delete_student)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Button for quitting the program
        self.quit_button = tk.Button(self, text='Quit', command=self.quit_program)
        self.quit_button.pack(pady=5)

        # Button for showing saved lists
        self.saved_lists_button = tk.Button(self, text='Saved Lists', command=self.show_saved_lists)
        self.saved_lists_button.pack(pady=5)

        self.update_student_listbox()  # Update the listbox with loaded student names

        self.selected_index = None  # To store the index of the selected item for editing

    # Method to add student names to the listbox
    def add_students(self):
        students_text = self.student_entry.get()
        if students_text:
            students = students_text.split(',')
            for student in students:
                student = student.strip()
                if student:
                    self.student_names.append(student)
                    self.student_listbox.insert(tk.END, student)
            self.save_student_names_to_file()  # Save updated student names to file
            self.student_entry.delete(0, tk.END)  # Clear entry after adding students

    # Method to toggle the shift status of a student name
    def toggle_shift_action(self):
        # Toggle shift for the selected student name
        selected_index = self.student_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            # Change background color of selected student name
            current_color = self.student_listbox.itemcget(index, "bg")
            new_color = "red" if current_color == "green" else "green"
            self.student_listbox.itemconfig(index, bg=new_color)

    # Method to edit a student name
    def edit_student(self):
        # Edit the selected student name
        self.selected_index = self.student_listbox.curselection()
        if self.selected_index:
            index = self.selected_index[0]
            new_name = self.student_entry.get()
            if new_name:
                self.student_names[index] = new_name
                self.student_listbox.delete(index)
                self.student_listbox.insert(index, new_name)
                self.save_student_names_to_file()  # Save updated student names to file
                self.selected_index = None
                self.student_entry.delete(0, tk.END)  # Clear entry after editing

    # Method to delete a student name
    def delete_student(self):
        # Delete the selected student name
        self.selected_index = self.student_listbox.curselection()
        if self.selected_index:
            index = self.selected_index[0]
            del self.student_names[index]
            self.student_listbox.delete(index)
            self.save_student_names_to_file()  # Save updated student names to file
            self.selected_index = None

    # Method to save the edited student name
    def save_student(self):
        self.edit_student()

    # Method to quit the program
    def quit_program(self):
        self.parent.destroy()  # Destroy the main window to quit the program

    # Method to show saved lists
    def show_saved_lists(self):
        # Show a messagebox with the saved lists
        if self.student_names:
            messagebox.showinfo("Saved Lists", "\n".join(self.student_names))
        else:
            messagebox.showinfo("Saved Lists", "No saved lists available")

    # Method to update the listbox with loaded student names
    def update_student_listbox(self):
        for name in self.student_names:
            self.student_listbox.insert(tk.END, name)

    # Method to load student names from file
    def load_student_names(self):
        try:
            with open("student_names.txt", "r") as file:
                self.student_names = file.read().splitlines()
        except FileNotFoundError:
            pass

    # Method to save updated student names to file
    def save_student_names_to_file(self):
        # Save updated student names to file
        with open("student_names.txt", "w") as file:
            file.write("\n".join(self.student_names))

# Entry point of the application
if __name__ == "__main__":
    app = LoginWindow()  # Create an instance of the login window
    app.mainloop()  # Start the main event loop
