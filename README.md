# Online Course App - Final Project

Django Online Course application with an assessment feature.

## Features
- Course and Lesson models
- Question, Choice and Submission models
- Django Admin integration
- Bootstrap course details page
- Mock exam submission
- Automatic score evaluation
- Exam result page with Congratulations message

## Run
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/admin/
