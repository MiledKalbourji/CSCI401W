# CSCI401W

Spring Semester Class at Rhode Island College Software Engineering of all Assignemnts and Final Project

Documentation:
teacher_project/
├── teacher/                        # Django project directory
│   ├── __init__.py
│   ├── settings.py                 # Django project settings
│   ├── urls.py                     # Main URL routing for the project
│   └── ...
└── attendance/                     # Django app directory for attendance management
    ├── migrations/                 # Database migrations
    ├── __init__.py
    ├── admin.py                    # Admin configurations for Django admin interface
    ├── models.py                   # Database models definition
    ├── serializers.py              # Serializers for API endpoints
    ├── urls.py                     # URL routing for API endpoints
    └── views.py                    # Views handling API logic

To start up on Mac: these 3 commands

source env/bin/activate

cd Teacher

python manage.py runserver
