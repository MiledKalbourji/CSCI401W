import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.username_frame = tk.Frame(self)
        self.username_frame.pack(padx=20, pady=5)
        
        self.username_label = tk.Label(self.username_frame, text='Username')
        self.username_label.pack(side=tk.LEFT)
        
        self.username_entry = tk.Entry(self.username_frame, textvariable=self.username)
        self.username_entry.pack(side=tk.LEFT)
        
        self.password_frame = tk.Frame(self)
        self.password_frame.pack(padx=20, pady=5)
        
        self.password_label = tk.Label(self.password_frame, text='Password')
        self.password_label.pack(side=tk.LEFT)
        
        self.password_entry = tk.Entry(self.password_frame, textvariable=self.password, show='*')
        self.password_entry.pack(side=tk.LEFT)
        
        self.login_button = tk.Button(self, text='Login', command=self.login)
        self.login_button.pack(pady=5)

    def login(self):
        username = self.username.get()
        password = self.password.get()
        # You can perform login authentication here
        print("Username:", username)
        print("Password:", password)
        # For demonstration, just print username and password
        
        # Get current day of the week
        now = datetime.now()
        day_of_week = now.strftime("%A")
        
        # Open student name window after successful login
        self.withdraw()  # Hide login window
        student_name_window = StudentNameWindow(self, day_of_week)
        student_name_window.wait_window()
        self.deiconify()  # Show login window again after student name window is closed
        self.destroy()  # Close the login window after opening the student name window

class StudentNameWindow(tk.Toplevel):
    def __init__(self, parent, day_of_week):
        super().__init__(parent)
        self.title("Student Name")
        self.parent = parent

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
        self.student_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.student_entry.focus()

        self.add_button = tk.Button(self.student_frame, text='Add', command=self.add_students)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.student_list_label = tk.Label(self, text='Student Names:')
        self.student_list_label.pack()

        self.student_listbox = tk.Listbox(self)
        self.student_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.edit_button = tk.Button(self, text='Edit', command=self.edit_student_name)
        self.edit_button.pack(pady=5)

        self.save_button = tk.Button(self, text='Save', command=self.save_student_name)
        self.save_button.pack(pady=5)

        self.quit_button = tk.Button(self, text='Quit', command=self.quit_program)
        self.quit_button.place(x=10, y=10)  # Position the Quit button in the top-left corner

        self.saved_lists_button = tk.Button(self, text='Saved Lists', command=self.show_saved_lists)
        self.saved_lists_button.place(x=10, y=40)  # Position the Saved Lists button below the Quit button

        self.update_student_listbox()  # Update the listbox with loaded student names

        self.selected_index = None  # To store the index of the selected item for editing

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

    def edit_student_name(self):
        selected_indices = self.student_listbox.curselection()
        if selected_indices:
            self.selected_index = selected_indices[0]
            selected_name = self.student_listbox.get(self.selected_index)
            self.student_entry.delete(0, tk.END)
            self.student_entry.insert(0, selected_name)

    def save_student_name(self):
        student_name = self.student_entry.get()
        if student_name:
            if self.selected_index is not None:
                self.student_names[self.selected_index] = student_name
                self.student_listbox.delete(self.selected_index)
                self.student_listbox.insert(self.selected_index, student_name)
                self.selected_index = None
            else:
                self.student_names.append(student_name)
                self.student_listbox.insert(tk.END, student_name)
            self.student_entry.delete(0, tk.END)  # Clear entry after saving
            self.save_student_names_to_file()  # Save updated student names to file
   
    def load_student_names(self):
        try:
            with open("student_names.txt", "r") as file:
                self.student_names = file.read().splitlines()
        except FileNotFoundError:
            pass

    def save_student_name(self):
        student_name = self.student_entry.get()
        if student_name:
            if self.selected_index is not None:
                self.student_names[self.selected_index] = student_name
                self.student_listbox.delete(self.selected_index)
                self.student_listbox.insert(self.selected_index, student_name)
                self.selected_index = None
            else:
                self.student_names.append(student_name)
                self.student_listbox.insert(tk.END, student_name)
            self.student_entry.delete(0, tk.END)  # Clear entry after saving
            self.save_student_names_to_file()  # Save updated student names to file

    def save_student_names_to_file(self):
        with open("student_names.txt", "w") as file:
            for name in self.student_names:
                file.write(name + "\n")

    def edit_student_name(self):
        selected_index = self.student_listbox.curselection()
        if selected_index:
            self.selected_index = selected_index[0]
            selected_name = self.student_listbox.get(self.selected_index)
            self.student_entry.delete(0, tk.END)
            self.student_entry.insert(0, selected_name)

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

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
