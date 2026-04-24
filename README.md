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
