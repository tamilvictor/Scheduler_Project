# Django Scheduler Microservice

This is a Django-based microservice for scheduling jobs. It allows users to create, retrieve, and manage scheduled jobs with customizable attributes. The service uses Django REST Framework for API endpoints and APScheduler for job scheduling.

## Features

- Create new jobs with customizable attributes.
- Retrieve a list of all scheduled jobs.
- Retrieve details of a specific job by ID.
- Schedule jobs to be executed at specified intervals.
- View and manage jobs through the Django admin interface.

## Technologies Used

- Django
- Django REST Framework
- APScheduler
- SQLite (default database)

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**
   git clone https://github.com/tamilvictor/Scheduler_Project.git
   cd scheduler_microservice

2.	Create a virtual environment:
python -m venv env
Activate the virtual environment:
.\env\Scripts\activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

The application will be accessible at http://127.0.0.1:8000/.

API Endpoints
1. List Jobs
•	Endpoint: GET /api/jobs/
•	Description: Retrieve a list of all scheduled jobs.
•	Response: JSON array of job objects.
2. Retrieve Job
•	Endpoint: GET /api/jobs/{id}/
•	Description: Retrieve details of a specific job by ID.
•	Response: JSON object of the job.
3. Create Job
•	Endpoint: POST /api/jobs/
•	Description: Create a new job.
•	Request Body:

{
    "name": "Email Notification",
    "description": "Send email notifications every hour.",
    "job_type": "email_notification",
    "interval": 3600,
    "parameters": {"email": "user@example.com"}
}
•	Response: JSON object of the created job.

Using the Django Admin Interface
1.	Access the admin interface at http://127.0.0.1:8000/admin/.
2.	Log in with your superuser account.
3.	Manage jobs through the "Jobs" section.


Testing the API
You can use tools like Postman or curl to test the API endpoints. Here are some example requests:

List Jobs
http://127.0.0.1:8000/api/jobs/

Retrieve Job
http://127.0.0.1:8000/api/jobs/{id}/

Create Job
"Content-Type: application/json" -d '{
    "name": "Email Notification",
    "description": "Send email notifications every hour.",
    "job_type": "email_notification",
    "interval": 3600,
    "parameters": {"email": "user@example.com"}
}' http://127.0.0.1:8000/api/jobs/

Acknowledgments
•	Django
•	Django REST Framework
•	APScheduler


