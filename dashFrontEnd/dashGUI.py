import dash
from dash import dcc, html, Input, Output, State
from datetime import datetime

# Initialize Dash app
app = dash.Dash(__name__)

# Define the layout of the Dash application
app.layout = html.Div([
    html.H1("Login"),  # Set the title of the window
    html.Label('Username'),  # Labels for username and password
    dcc.Input(id='username', type='text'),  # Input field for username
    html.Label('Password'),
    dcc.Input(id='password', type='password'),  # Input field for password
    html.Button('Login', id='login-button'),  # Button for logging in
    html.Div(id='output-login'),  # Div to display login output
    html.Button('Create Account', id='create-account-button'),  # Button for creating a new account
    html.Div(id='output-create-account'),  # Div to display create account output
    html.Div(id='student-name-window'),  # Div to display student name window
    html.Button('Quit', id='quit-button'),  # Button to quit the program
])

# Define callback to handle login
@app.callback(
    Output('output-login', 'children'),
    [Input('login-button', 'n_clicks')],
    [State('username', 'value'), State('password', 'value')]
)
def update_output_login(n_clicks, username, password):
    if n_clicks:
        # You can perform login authentication here
        print("Username:", username)
        print("Password:", password)
        
        # Get current day of the week
        now = datetime.now()
        day_of_week = now.strftime("%A")
        
        # Return some output
        return f"Logged in! Today is {day_of_week}!"

# Define callback to handle creating a new account
@app.callback(
    Output('output-create-account', 'children'),
    [Input('create-account-button', 'n_clicks')],
)
def update_output_create_account(n_clicks):
    if n_clicks:
        return html.Div([
            html.H2("Create Account"),
            html.Label("Enter your details:"),
            html.Div([
                html.Label('First Name'),
                dcc.Input(id='first-name', type='text'),
                html.Label('Last Name'),
                dcc.Input(id='last-name', type='text'),
                html.Label('Email'),
                dcc.Input(id='email', type='email'),
                html.Label('Password'),
                dcc.Input(id='new-password', type='password'),
                html.Button('Submit', id='submit-account-button'),
                html.Div(id='output-submit-account')
            ])
        ])

# Define callback to handle submission of account creation
@app.callback(
    Output('output-submit-account', 'children'),
    [Input('submit-account-button', 'n_clicks')],
    [State('first-name', 'value'), State('last-name', 'value'), State('email', 'value'), State('new-password', 'value')]
)
def update_output_submit_account(n_clicks, first_name, last_name, email, new_password):
    if n_clicks:
        # You can perform further processing with the entered account details here
        return f"Account created successfully for {first_name} {last_name} with email {email}."

# Define callback to display student name window after successful login
@app.callback(
    Output('student-name-window', 'children'),
    [Input('login-button', 'n_clicks')],
    [State('username', 'value'), State('password', 'value')]
)
def display_student_name_window(n_clicks, username, password):
    if n_clicks:
        # Assuming successful login, display the student name window
        return html.Div([
            html.H2("Student Name"),
            html.Label("Enter student names separated by comma:"),
            dcc.Input(id='student-names-input', type='text'),
            html.Button('Add', id='add-student-button'),
            html.Div(id='student-list-div', children=[
                html.H3("Student Names"),
                html.Ul(id='student-list')
            ]),
            html.Button('Edit', id='edit-student-button'),
            html.Button('Save', id='save-student-button'),
            html.Button('Delete', id='delete-student-button'),
            html.Button('Load', id='load-student-button'),
        ])

# Define callback to add student names to the list
@app.callback(
    Output('student-list', 'children'),
    [Input('add-student-button', 'n_clicks')],
    [State('student-names-input', 'value'), State('student-list', 'children')]
)
def add_student_names(n_clicks, student_names_input, current_names):
    if n_clicks and student_names_input:
        names = student_names_input.split(',')
        new_names = [html.Li(name.strip()) for name in names]
        return current_names + new_names if current_names else new_names

# Define callback to handle quitting the program
@app.callback(
    Output('quit-message', 'children'),
    [Input('quit-button', 'n_clicks')]
)
def quit_program(n_clicks):
    if n_clicks:
        raise dash.exceptions.PreventUpdate

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
