
# Bloggy

Bloggy is a simple Django-based blogging platform designed to make it easy to create and manage a blog.

![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)
![Django Version](https://img.shields.io/badge/django-3.2-green.svg)
![GitHub](https://img.shields.io/github/license/kpardhasai2004/Gallery_v1)
![GitHub last commit](https://img.shields.io/github/last-commit/kpardhasai2004/Gallery_v1)
![GitHub issues](https://img.shields.io/github/issues-raw/kpardhasai2004/Gallery_v1)


**Live Link:** [https://blogy.pythonanywhere.com/](https://blogy.pythonanywhere.com/)

## Features

- Create, edit, and delete blog posts.
- User authentication and authorization.
- User-friendly admin interface.
- Markdown support for rich content creation.
- Responsive design for various screen sizes.
- Commenting system for engaging with readers.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9
- Django 3.2

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/kpardhasai2004/bloggy.git
   cd bloggy
   ```

2. Create a virtual environment and activate it (optional but recommended):

   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```shell
   python manage.py migrate
   ```

5. Create a superuser account:

   ```shell
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. Access the admin interface at `http://localhost:8000/admin/` and log in with your superuser credentials to start managing your blog.

## Usage

Explain how to use the application, including creating, editing, and deleting blog posts. Also, provide information about the Markdown support and commenting system.

## Deployment

Add instructions for deploying this application to a production server, including any specific server requirements and configuration.
