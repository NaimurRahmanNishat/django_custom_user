# Django Custom User Project

This project implements a **Custom User Model** in Django, replacing the default Django User model. This is a best practice for Django projects, allowing for more flexibility (like using an Email instead of a Username for login) and adding custom fields to user profiles from the start.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setting Up the Virtual Environment](#setting-up-the-virtual-environment)
- [Database Migrations](#database-migrations)
- [Running the Server](#running-the-server)
- [Usage](#usage)
- [Contributing](#contributing)

---

## Features
* **Custom User Model:** Inherits from `AbstractUser` or `AbstractBaseUser`.
* **Email Authentication:** Configured to use Email as the primary unique identifier.
* **Scalability:** Easily add extra fields (e.g., date of birth, profile picture) to the User model.
* **Admin Integration:** Custom User admin interface to manage users easily.

## Prerequisites
Before you begin, ensure you have:
* **Python 3.8+** installed.
* **Git** installed on your system.
* A basic understanding of the Django framework and its authentication system.

## Installation
First, clone the repository to your local machine:

```bash
https://github.com/NaimurRahmanNishat/django_custom_user.git
cd django_custom_user
```

## Setting Up the Virtual Environment
It is recommended to use a virtual environment to keep dependencies isolated.

On Windows:
```bash
python -m venv myenv
source myenv/Scripts/activate (using git bash)
```

On macOS/Linux:
```bash
python -m venv myenv
source myenv/bin/activate 
```

Installation django
```bash
pip install django
```

Install Dependencies:
```bash
pip install -r requirements.txt
```

## Database Migrations
Since this project uses a custom user model, applying migrations is crucial for setting up the authentication tables correctly.
```bash
python manage.py makemigrations
python manage.py migrate
```

Create a Superuser to access the Django Admin panel:
```bash
python manage.py createsuperuser
```

## Running the Server
To start the development server, run:
```bash
python manage.py runserver
```
You can now access the project at http://127.0.0.1:8000/.

## Usage
1. **Admin Panel:** Go to http://127.0.0.1:8000/admin and log in with your superuser credentials.
2. **User Management:** Notice how the user model behaves differently than the default (e.g., using Email instead of Username).
3. **Customization:** To add more fields, check the `models.py` file in your users app.

## Contributing
Contributions are always welcome! 

1. **Fork** the project.
2. **Create** your feature branch:  
   `git checkout -b feature/NewFeature`
3. **Commit** your changes:  
   `git commit -m 'Add some NewFeature'`
4. **Push** to the branch:  
   `git push origin feature/NewFeature`
5. **Open** a Pull Request.

## Created by [Naimur Rahman Nishat] [GitHub Profile](https://github.com/NaimurRahmanNishat)
