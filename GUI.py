/*
 * File: FrontEnd GUI
 * The program, once executed, is going to prompt the user, a label for Username/Password with text box and functional button for the login button
 * Login button automatically pops up a new window 
 * CSCI401W
 * Author: Miled Kalbourji
 */

import tkinter as tk
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
        self.geometry("300x200")

        # Welcome message label
        self.welcome_label = tk.Label(self, text=f"Welcome! Today is {day_of_week}!", font=("Arial", 14, "bold"))
        self.welcome_label.pack(pady=10)

        self.student_names = []  # List to store student names
        self.load_student_names()  # Load saved student names

        self.student_label = tk.Label(self, text='Student Name', fg='gray')
        self.student_label.pack()

        self.student_entry = tk.Entry(self)
        self.student_entry.pack()
        self.student_entry.focus()

        self.save_button = tk.Button(self, text='Save', command=self.save_student_name)
        self.save_button.pack(pady=5)

        self.student_list_label = tk.Label(self, text='Student Names:')
        self.student_list_label.pack()

        self.student_listbox = tk.Listbox(self)
        self.student_listbox.pack()

        self.quit_button = tk.Button(self, text='Quit', command=self.quit_program)
        self.quit_button.place(x=10, y=10)  # Position the Quit button in the top-left corner

        self.saved_lists_button = tk.Button(self, text='Saved Lists', command=self.show_saved_lists)
        self.saved_lists_button.place(x=10, y=40)  # Position the Saved Lists button below the Quit button

        self.update_student_listbox()  # Update the listbox with loaded student names

    def load_student_names(self):
        try:
            with open("student_names.txt", "r") as file:
                self.student_names = file.read().splitlines()
        except FileNotFoundError:
            pass

    def save_student_name(self):
        student_name = self.student_entry.get()
        if student_name:
            self.student_names.append(student_name)
            self.student_listbox.insert(tk.END, student_name)
            self.student_entry.delete(0, tk.END)  # Clear entry after saving
            self.save_student_names_to_file()  # Save updated student names to file

    def save_student_names_to_file(self):
        with open("student_names.txt", "w") as file:
            for name in self.student_names:
                file.write(name + "\n")

    def quit_program(self):
        self.parent.destroy()  # Destroy the main window to quit the program

    def show_saved_lists(self):
        # Show a messagebox with the saved lists
        if self.student_names:
            tk.messagebox.showinfo("Saved Lists", "\n".join(self.student_names))
        else:
            tk.messagebox.showinfo("Saved Lists", "No saved lists available")

    def update_student_listbox(self):
        for name in self.student_names:
            self.student_listbox.insert(tk.END, name)

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()



