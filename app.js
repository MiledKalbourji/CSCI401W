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
        document.getElementById('login-feedback').innerHTML = 'Login successful!';
        document.getElementById('student-name-window').style.display = 'block';
        document.getElementById('login-window').style.display = 'none';
        document.getElementById('login-button').style.display = 'none';
        document.getElementById('create-account-button').style.display = 'none';
        document.getElementById('sign-out-button').style.display = 'block'; // Show sign-out button
        document.getElementById('save-students-button').style.display = 'block'; // Show the Save Students button
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

function addStudent(name) {
    if (name) {
        let listDiv = document.getElementById('student-list-div');
        let div = document.createElement('div');
        div.classList.add('student');

        let nameLabel = document.createElement('span');
        nameLabel.textContent = name;
        nameLabel.className = 'student-name';
        div.appendChild(nameLabel);

        let editButton = document.createElement('button');
        editButton.textContent = 'Edit';
        editButton.onclick = function() {
            if (editButton.textContent === 'Edit') {
                let input = document.createElement('input');
                input.type = 'text';
                input.value = nameLabel.textContent;
                div.insertBefore(input, nameLabel);
                div.removeChild(nameLabel);
                editButton.textContent = 'Save';
            } else {
                nameLabel.textContent = div.querySelector('input').value;
                div.insertBefore(nameLabel, div.querySelector('input'));
                div.removeChild(div.querySelector('input'));
                editButton.textContent = 'Edit';
            }
        };
        div.appendChild(editButton);

        let deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = function() {
            div.remove();
        };
        div.appendChild(deleteButton);

        let toggleButton = createToggleButton();
        div.appendChild(toggleButton);

        listDiv.appendChild(div);
    }
}

function createToggleButton() {
    let toggleButton = document.createElement('button');
    toggleButton.textContent = 'Absent'; // Default state
    toggleButton.classList.add('toggle-button', 'absent');
    toggleButton.onclick = function() {
        toggleButton.textContent = (toggleButton.textContent === 'Present' ? 'Absent' : 'Present');
        toggleButton.classList.toggle('present');
        toggleButton.classList.toggle('absent');
    };
    return toggleButton;
}

function saveStudents() {
    let students = [];
    document.querySelectorAll('.student .student-name').forEach(function(elem) {
        students.push(elem.textContent);
    });
    localStorage.setItem('students', JSON.stringify(students));
    alert('Students saved successfully!');
}

// Function to load students from localStorage on page load
function loadStudents() {
    let students = JSON.parse(localStorage.getItem('students'));
    if (students) {
        students.forEach(function(name) {
            addStudent(name);
        });
    }
}

loadStudents(); // Load students when the page loads