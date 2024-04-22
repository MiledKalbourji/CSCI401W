import dash
from dash import dcc, html, Input, Output, State
from dash.dependencies import ALL
from datetime import datetime

# Initialize Dash app with suppress_callback_exceptions=True
app = dash.Dash(__name__, suppress_callback_exceptions=True, prevent_initial_callbacks=True, external_stylesheets=['/assets/styles.css'])

# Define the layout with two buttons and placeholder divs for login and create account windows
app.layout = html.Div([
    html.H1("Welcome To the Teacher App"),
    html.Button('Login', id='login-button', n_clicks=0),
    html.Button('Create Account', id='create-account-button', n_clicks=0),
    html.Div(id='login-window', className='login-window'),  # Placeholder for login window content
    html.Div(id='create-account-window', className='create-account-window'),  # Placeholder for create account window content
    html.Div(id='output-login'),  # Placeholder for login output
    html.Div(id='student-name-window', className='student-name-window'),  # Placeholder for student name window content
    html.Div(id='output-submit-account'),  # Placeholder for account submission output
])

# Define callback to display login window when login button is clicked
@app.callback(
    Output('login-window', 'children'),
    [Input('login-button', 'n_clicks')]
)
def display_login_window(n_clicks):
    if n_clicks:
        return html.Div([
            html.H2("Login Window"),
            html.Label('Username'),
            dcc.Input(id='username', type='text', value=''),
            html.Label('Password'),
            dcc.Input(id='password', type='password', value=''),
            html.Button('Login', id='submit-login-button', className='button button-login')
        ])
# Define callback to handle login
@app.callback(
    Output('output-login', 'children'),
    [Input('submit-login-button', 'n_clicks')],
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
    
# Define callback to display student name window after successful login
@app.callback(
    Output('student-name-window', 'children'),
    [Input('submit-login-button', 'n_clicks')],
    [State('username', 'value'), State('password', 'value')]
)
def display_student_name_window(n_clicks, username, password):
    if n_clicks and username and password:
        # Assuming successful login, display the student name window
        return html.Div([
            html.H2("Student Name"),
            html.Label("Enter student names separated by comma:"),
            dcc.Input(id='student-names-input', type='text'),
            html.Button('Add', id='add-student-button'),
            html.Div(id='student-list-div'),
        ])
    else:
        return html.Div()  # Return an empty div if login was not successful or inputs are empty

# Define callback to add student names to the list
@app.callback(
    Output('student-list-div', 'children'),
    [Input('add-student-button', 'n_clicks')],
    [State('student-names-input', 'value')]
)
def add_student_names(n_clicks, student_names_input):
    if n_clicks and student_names_input:
        names = student_names_input.split(',')
        student_list = [html.Div([
            html.Label(name.strip(), id={'type': 'shift-label', 'index': name.strip()}),
            html.Button('Toggle Shift', id={'type': 'shift-button', 'index': name.strip()})
        ]) for name in names]
        return student_list

# Define callback to toggle shift label for each student
@app.callback(
    Output({'type': 'shift-label', 'index': ALL}, 'children'),
    [Input({'type': 'shift-button', 'index': ALL}, 'n_clicks')],
    [State({'type': 'shift-label', 'index': ALL}, 'children')]
)
def toggle_shift(n_clicks_list, current_labels):
    new_labels = []
    for n_clicks, label_text in zip(n_clicks_list, current_labels):
        # Toggle the IN/OUT label based on the number of clicks
        if n_clicks is None:
            new_label = 'IN'  # Default to IN if n_clicks is None
        elif n_clicks % 2 == 0:
            new_label = 'OUT'
        else:
            new_label = 'IN'

        # Check if label_text is already a list
        if isinstance(label_text, list):
            # Construct the new label text without altering the structure of the student name
            new_label_text = [html.Label(new_label, className='right-align-label')] + label_text[1:]
        else:
            # If label_text is a string, wrap it in a list with the new label
            new_label_text = [html.Label(new_label, className='right-align-label'), html.Label(label_text)]

        new_labels.append(new_label_text)  # Append the new label to the list of labels

    return new_labels

# Define callback to display create account window when create account button is clicked
@app.callback(
    Output('create-account-window', 'children'),
    [Input('create-account-button', 'n_clicks')],
    allow_duplicate=True  # Set allow_duplicate to True
)
def display_create_account_window(n_clicks):
    if n_clicks:
        return html.Div([
            html.H2("Create Account Window"),
            html.Label("Enter your details:"),
            html.Label('First Name'),
            dcc.Input(id='first-name', type='text'),
            html.Label('Last Name'),
            dcc.Input(id='last-name', type='text'),
            html.Label('Email'),
            dcc.Input(id='email', type='email'),
            html.Label('Password'),
            dcc.Input(id='new-password', type='password'),
            html.Button('Submit', id='submit-account-button', className='button button-create-account')
        ])

# Define callback to handle submission of account creation and redirect to login popup
@app.callback(
    [Output('output-submit-account', 'children'),
     Output('create-account-window', 'style'),
     Output('login-button', 'n_clicks')],
    [Input('submit-account-button', 'n_clicks')],
    [State('first-name', 'value'), State('last-name', 'value'), State('email', 'value'), State('new-password', 'value')]
)
def update_output_submit_account(n_clicks, first_name, last_name, email, new_password):
    if n_clicks:
        # You can perform further processing with the entered account details here
        # For demonstration, let's print the account details
        print(f"Account created successfully for {first_name} {last_name} with email {email}.")
        
        # Hide the create account window
        create_account_window_style = {'display': 'none'}
        
        # Set the number of clicks for the login button to open the login popup
        login_button_n_clicks = 1
        
        # Return the message indicating successful account creation, the updated style for the create account window,
        # and the number of clicks for the login button
        return f"Account created successfully for {first_name} {last_name} with email {email}.", create_account_window_style, login_button_n_clicks
    else:
        # Return initial values if no submission has been made
        return dash.no_update, dash.no_update, dash.no_update

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
