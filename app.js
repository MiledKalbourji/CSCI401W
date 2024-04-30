// Ensure all DOM content is loaded before executing scripts
document.addEventListener('DOMContentLoaded', function() {
    // Login, Create Account, and Sign-out button functionality
    document.getElementById('login-button').addEventListener('click', function() {
        toggleVisibility('login-window');
        document.getElementById('create-account-window').style.display = 'none';
        document.getElementById('output-submit-account').style.display = 'none'; // Hide account creation message
        document.getElementById('add-students-button').addEventListener('click', addStudents);
        document.getElementById('save-students-button').addEventListener('click', saveStudents);
    });

    document.getElementById('create-account-button').addEventListener('click', function() {
        toggleVisibility('create-account-window');
        document.getElementById('login-window').style.display = 'none';
        document.getElementById('output-login').style.display = 'none'; // Clear login feedback
    });

    document.getElementById('sign-out-button').addEventListener('click', function() {
        // Hide all sensitive information and buttons
        document.getElementById('student-name-window').style.display = 'none';
        document.getElementById('login-button').style.display = 'block';
        document.getElementById('create-account-button').style.display = 'block';
        document.getElementById('sign-out-button').style.display = 'none';
        document.getElementById('save-students-button').style.display = 'none'; // Hide the Save Students button
        document.getElementById('login-feedback').innerHTML = ''; // Clear any feedback message
    });
    

    // Login submission
    document.getElementById('submit-login').addEventListener('click', submitLogin);

    // Account creation submission
    document.getElementById('submit-account').addEventListener('click', submitAccount);

    // Add students
    document.getElementById('add-students-button').addEventListener('click', addStudents);
});

// Toggle visibility of elements
function toggleVisibility(elementId) {
    var element = document.getElementById(elementId);
    element.style.display = (element.style.display === 'block' ? 'none' : 'block');
}

// Handle login functionality
function submitLogin() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let storedUsername = localStorage.getItem('username');
    let storedPassword = localStorage.getItem('password');

    if (username === storedUsername && password === storedPassword) {
        localStorage.setItem('currentUser', username); // Store current user
        window.location.href = 'attendance.html'; // Redirect to the attendance page
    } else {
        document.getElementById('login-feedback').innerHTML = 'Invalid username or password!';
    }
}

// Handle account creation functionality
function submitAccount() {
    let firstName = document.getElementById('first-name').value;
    let lastName = document.getElementById('last-name').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('new-password').value;

    localStorage.setItem('username', email); // Using email as username
    localStorage.setItem('password', password);

    document.getElementById('output-submit-account').innerHTML = `Account created for ${firstName} ${lastName}! Sign In!`;
    document.getElementById('output-submit-account').style.display = 'block';
    document.getElementById('create-account-window').style.display = 'none';
}

function addStudents() {
    let input = document.getElementById('student-names-input').value;
    let names = input.split(',');
    let listDiv = document.getElementById('student-list-div');

    names.forEach(function(name) {
        addStudent(name.trim());
    });

    document.getElementById('student-names-input').value = ''; // Clear the input field after adding
}


loadStudents(); // Load students when the page loads