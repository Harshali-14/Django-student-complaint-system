# Complaint Management System

A web-based **Complaint Management System** developed using **Django** and **MySQL** that enables users to submit, manage, and track complaints efficiently through a secure and user-friendly platform.

The system provides role-based access for users and administrators, ensuring smooth complaint handling, status monitoring, and effective resolution management.

---

## Features

### User Authentication
- User Registration
- User Login & Logout
- Secure Authentication System
- Profile Management

### Complaint Management
- Submit New Complaints
- View Complaint Details
- Update Complaint Information
- Delete Complaints
- Manage Complaint Records

### Complaint Status Tracking
- Pending Status
- In Progress Status
- Resolved Status
- Real-Time Status Updates

### Admin Dashboard
- Manage User Complaints
- Update Complaint Status
- Monitor Complaint Activities
- View Complaint Statistics
- Complaint Overview Dashboard

### Search and Filtering
- Search Complaints by Keywords
- Filter Complaints by Status
- Quick Access to Complaint Records

### Responsive User Interface
- Clean and Modern Design
- Mobile-Friendly Layout
- Responsive Across Devices

---

## Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Programming |
| Django | Web Framework |
| MySQL | Database Management |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| Bootstrap | Responsive Design |
| JavaScript | Client-Side Functionality |

---

## Project Structure

```bash
Complaint-Management-System/
│
├── complaint_system/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
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

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Complaint-Management-System.git

cd Complaint-Management-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

#### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Configuration

Update the database settings inside `settings.py`.

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

## Apply Migrations

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

## Run the Application

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## Screenshots

### Register Page
![Register](Screenshots/register.png)

### Login Page
![Login](Screenshots/login.png)

### About Page
![About](Screenshots/about_us.png)

### User Profile
![Profile](Screenshots/profilepage.png)

### Complaint Dashboard
![Dashboard](Screenshots/complaints_dashboard.png)

### View Complaints
![View Complaints](Screenshots/viewcomplaint.png)

### Update Complaint
![Update Complaint](Screenshots/updatepage.png)

---

## Security Features

- Password Hashing
- CSRF Protection
- Secure Authentication
- Session Management
- Django Built-in Security Features

---

## Key Highlights

- Role-Based Access Control
- Complaint Lifecycle Management
- Complaint Status Tracking
- Responsive User Interface
- Secure Data Handling
- Admin Monitoring Dashboard

---

## Future Enhancements

- Email Notifications
- SMS Notifications
- Analytics Dashboard
- AI-Based Complaint Classification
- Complaint Priority Levels
- Complaint Assignment System
- Report Generation

---

## Author

**Harshali Kulkarni**  
MCA Student | Python Developer | Django Developer

---

## License

This project is developed for educational and learning purposes.
