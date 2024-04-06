# Front end application 

# Author: Miled kalbourji

import tkinter as tk
from tkinter import simpledialog, messagebox
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

        tk.Label(self, text="Email:").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

         # Create the password frame
        self.password_frame = tk.Frame(self)
        self.password_frame.pack(pady=10)

        tk.Label(self.password_frame, text="Password:").pack()
        self.password_entry = tk.Entry(self.password_frame, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Submit", command=self.submit_account).pack()  # Button to submit the account information

    # Method to handle the submit button click event
    def submit_account(self):
        # Get account information from entry fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        # Process account creation (store information, etc.)
        print("Account Information:")
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Password:", password)
        print("Email:", email)

        # Close the window
        self.destroy()

class StudentNameWindow(tk.Toplevel):
    def __init__(self, parent, day_of_week):
        super().__init__(parent)
        self.title("Student Name")
        self.parent = parent
        self.configure(bg="red")  # Set background color to red 

        # Set window size
        self.geometry("400x300")

        # Welcome message label
        self.welcome_label = tk.Label(self, text=f"Welcome! Today is {day_of_week}!", font=("Arial", 14, "bold"))
        self.welcome_label.pack(pady=10)

        self.student_names = []  # List to store student names
        self.load_student_names()  # Load saved student names

        self.student_frame = tk.Frame(self)
        self.student_frame.pack(pady=5)

        self.student_label = tk.Label(self.student_frame, text='Student Name', fg='gray')
        self.student_label.pack(side=tk.LEFT)

        self.student_entry = tk.Entry(self.student_frame)
        self.student_entry.pack(side=tk.LEFT, padx=5)
        self.student_entry.focus()

        self.add_button = tk.Button(self.student_frame, text='Add', command=self.add_students)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.student_list_label = tk.Label(self, text='Student Names:')
        self.student_list_label.pack()

        self.student_listbox = tk.Listbox(self, bg="lightgreen")  # Set default background color to light green
        self.student_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        self.student_listbox.bind('<Button-1>', self.toggle_shift)

        # Edit, Save, and Delete buttons
        self.edit_button = tk.Button(self, text='Edit', command=self.edit_student)
        self.edit_button.pack(side=tk.LEFT, padx=5)
        self.save_button = tk.Button(self, text='Save', command=self.save_student)
        self.save_button.pack(side=tk.LEFT, padx=5)
        self.delete_button = tk.Button(self, text='Delete', command=self.delete_student)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.quit_button = tk.Button(self, text='Quit', command=self.quit_program)
        self.quit_button.pack(pady=5)

        self.saved_lists_button = tk.Button(self, text='Saved Lists', command=self.show_saved_lists)
        self.saved_lists_button.pack(pady=5)

        self.update_student_listbox()  # Update the listbox with loaded student names

        self.selected_index = None  # To store the index of the selected item for editing
        self.original_bg_color = None  # To store the original background color of the selected item

    def add_students(self):
        students_text = self.student_entry.get()
        if students_text:
            students = students_text.split(',')
            for student in students:
                student = student.strip()
                if student:
                    self.student_names.append(student)
                    self.student_listbox.insert(tk.END, student)
            self.student_entry.delete(0, tk.END)  # Clear entry after adding students
    
    def toggle_shift(self, event):
        # Clear any existing toggle shift buttons
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget('text') == 'Toggle Shift':
                widget.destroy()

        # Get the index of the clicked item in the listbox
        index = self.student_listbox.nearest(event.y)

        # Check if the index is valid
        if index != -1:
            # Get the text of the clicked item
            student_name = self.student_listbox.get(index)

            # Add a toggle shift button next to the selected student name
            toggle_shift_button = tk.Button(self, text='Toggle Shift')
            toggle_shift_button.bind('<Button-1>', lambda event, student=student_name: self.toggle_shift_action(student))
            toggle_shift_button.place(relx=1, rely=0, anchor=tk.NE)

    def toggle_shift_action(self, student_name):
        # Toggle shift for the selected student
        print(f"Toggle Shift for {student_name}")
        # Find the index of the student name in the listbox
        index = self.student_listbox.get(0, tk.END).index(student_name)
        # Get the current background color of the student name
        current_bg = self.student_listbox.itemcget(index, 'bg')
        # Toggle the background color
        new_bg = 'lightgreen' if current_bg == 'red' else 'red'
        # Change the background color of the student name
        self.student_listbox.itemconfig(index, {'bg': new_bg})
        
    def edit_student(self):
        # Get the index of the selected item in the listbox
        index = self.student_listbox.curselection()
        if index:
            index = int(index[0])
            student_name = self.student_listbox.get(index)
            # Get the current background color of the selected item
            self.original_bg_color = self.student_listbox.itemcget(index, 'bg')
            # Ask for the new student name
            new_name = tk.simpledialog.askstring("Edit Student", "Enter new name:", initialvalue=student_name)
            if new_name:
                self.student_listbox.delete(index)
                self.student_listbox.insert(index, new_name)
                # Reset the background color to its original state
                self.student_listbox.itemconfig(index, {'bg': self.original_bg_color})
                self.student_names[index] = new_name

    def save_student(self):
        # Get the index of the selected item in the listbox
        index = self.student_listbox.curselection()
        if index:
            index = int(index[0])
            student_name = self.student_listbox.get(index)
            # Save the student name to a file
            with open("student_names.txt", "a") as file:
                file.write(student_name + "\n")
            messagebox.showinfo("Save", "Student name saved successfully.")

    def delete_student(self):
        # Get the index of the selected item in the listbox
        index = self.student_listbox.curselection()
        if index:
            index = int(index[0])
            student_name = self.student_listbox.get(index)
            # Remove the student name from the list and listbox
            del self.student_names[index]
            self.student_listbox.delete(index)
            messagebox.showinfo("Delete", "Student name deleted successfully.")

    def quit_program(self):
        self.parent.destroy()  # Destroy the main window to quit the program

    def show_saved_lists(self):
        # Show a messagebox with the saved lists
        if self.student_names:
            messagebox.showinfo("Saved Lists", "\n".join(self.student_names))
        else:
            messagebox.showinfo("Saved Lists", "No saved lists available")

    def update_student_listbox(self):
        for name in self.student_names:
            self.student_listbox.insert(tk.END, name)

    def load_student_names(self):
        try:
            with open("student_names.txt", "r") as file:
                self.student_names = file.read().splitlines()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
