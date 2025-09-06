Django Library Management System
This is a web application built with the Django framework to manage a small library's catalog, members, and book borrowing transactions. It provides a simple, clean interface for users to check the availability of books, view their transaction history, and borrow new books.

Features
User Authentication: Secure signup, login, and logout functionality.

Dashboard Overview: A clean dashboard displaying key metrics like total books, available books, total members, and borrowed and overdue books.

Book Management: Admins can add, update, and delete books through the Django Admin panel.

Transaction Management: Users can borrow available books, and admins can manually mark books as returned from the admin interface.

Personalized Accounts: Users can view their personal account details and a history of all their transactions.

Responsive Design: The application is built with Tailwind CSS for a modern and mobile-friendly user interface.

Technology Stack
Backend: Python, Django

Database: MySQL

Frontend: HTML, Tailwind CSS, JavaScript

Deployment: The project is configured for deployment on platforms like Render.

Getting Started
Prerequisites
Python 3.13+

pip (Python package installer)

A MySQL database server

1. Clone the repository
git clone [https://github.com/your-username/library-management-system.git](https://github.com/your-username/library-management-system.git)
cd library-management-system

2. Set up a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

3. Install dependencies
Install all the required packages from the requirements.txt file.

pip install -r requirements.txt

4. Configure the database
Update the DATABASES setting in library_project/settings.py with your MySQL credentials.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
(note: the above is during development using mysql, later for deployment change it as per your host)  

5. Run migrations
Apply the initial database migrations to create the necessary tables.

python manage.py makemigrations
python manage.py migrate

6. Create a superuser
This will allow you to access the Django Admin panel to add books and manage data.

python manage.py createsuperuser

7. Run the development server
python manage.py runserver

The application will be available at http://127.0.0.1:8000/.(before deployment)

Deployment on Render
This project is configured for deployment on Render using environment variables for sensitive data. You will need to:

Set DEBUG to False and ALLOWED_HOSTS to your Render URL.

Configure the SECRET_KEY and DATABASE_URL as environment variables on the Render dashboard.

Contact
If you have any questions or feedback, please feel free to reach out.
