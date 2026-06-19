# ResolveX – Complaint Management System

A web-based **Complaint Management System** developed using **Django** and **MySQL** that enables users to submit, manage, and track complaints through a secure and structured platform.

The system provides role-based access for users and administrators, ensuring efficient complaint handling, status tracking, and resolution management.

---

## Live Demo

https://resolvex-x1ka.onrender.com/

---

## Features

### User Authentication

* User registration
* Secure login and logout
* Profile management

### Complaint Management

* Submit new complaints
* View complaint details
* Update complaints
* Delete complaints
* Manage complaint records

### Complaint Status Tracking

* Pending
* In Progress
* Resolved
* Real-time status updates

### Admin Dashboard

* Manage user complaints
* Update complaint status
* Monitor all complaints
* View complaint statistics
* Complaint overview dashboard

### Search and Filtering

* Search complaints by keywords
* Filter by status
* Quick access to records

### Responsive Interface

* Clean and modern UI
* Mobile-friendly design
* Fully responsive layout

---

## Technology Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Backend development       |
| Django     | Web framework             |
| MySQL      | Database management       |
| HTML5      | Frontend structure        |
| CSS3       | Styling                   |
| Bootstrap  | Responsive design         |
| JavaScript | Client-side functionality |

---

## Project Structure

```bash
Complaint-Management-System/
│
├── complaint_system/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── complaints/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── Screenshots/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Harshali-14/Django-Student-Complaint-System.git
cd Django-Student-Complaint-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Configuration

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'complaint_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Project

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## Screenshots

* Register Page
* Login Page
* About Page
* User Profile
* Complaint Dashboard
* View Complaints
* Update Complaint

(Stored inside `/Screenshots` folder)

---

## Security Features

* Password hashing
* CSRF protection
* Secure authentication system
* Session management
* Django security middleware

---

## Key Features

* Role-based access control
* Complaint lifecycle management
* Status tracking system
* Admin control dashboard
* Responsive UI design
* Secure data handling

---

## Future Enhancements

* Email notifications
* SMS notifications
* Analytics dashboard
* AI-based complaint classification
* Priority-based complaints
* Assignment system
* PDF report generation
* Activity logs

---

## Author

Harshali Kulkarni
MCA Student | Python Developer | Django Developer

---

## License

This project is created for educational and learning purposes.
