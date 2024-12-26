# Django

Django is a framework designed for building web applications.
Django is commonly used for backend development, such as building e-commerce applications.
Known as a "batteries-included" framework, it provides tools out of the box, including

- Admin Site
- Object-Relational Mapper (ORM)
- Authentication
- Caching

## Prerequisites

Before starting with Django, ensure familiarity with the following:

- Python: Basic knowledge, including Object-Oriented Programming (OOP) concepts like classes, inheritance, and polymorphism.
- Databases: Understanding of relational databases.

## Understanding HTTP

HTTP (HyperText Transfer Protocol) defines how the client (browser) communicates with the server.

1. When a user enters a URL and presses Enter, the browser sends a request to the server for the home page.
2. The server responds with the requested page.
3. As users navigate through the site, the browser sends new requests to the server for each page.

## Installing Django

- Ensure Python 3 and pip are installed on your system.
- install Django using pipenv

```bash
 pipenv install django
```

- Activate the virtual environment with:

```bash
pipenv shell
```

### Using django-admin

- django-admin is a utility tool provided by Django.
- To see the available commands, run:

```bash
django-admin
```

### Starting a Django Project

run:

```bash
django-admin startproject project-name
```

Alternatively, to avoid creating two directories (one for the project and another for the core files),
run:

```bash
django-admin startproject storefront .
python manage.py runserver 9000
```

The server will run at:
http://localhost:9000

## django-apps

A Django project is essentially a collection of various apps, with each app offering specific functionality.
Just like apps in mobile phone, each app provides a certain functionality.
In project oppen settings and there are some apps

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Every Django project includes several default apps that provide essential functionality out of the box:

- Admin App: Offers an admin interface for managing the project's data.
- Auth App: Handles user authentication and authorization, including user login, logout, and permissions.
- ContentTypes App: Provides a framework for working with generic relationships and content types in the database.
- Sessions App: Manages sessions to store data about individual user sessions across requests.
- Messages App: Enables temporary notifications (e.g., success or error messages) to be displayed to users.
- StaticFiles App: Simplifies serving static files, such as images, CSS, and JavaScript.
- Each app contributes a specific piece of functionality to the project, allowing developers to build robust and scalable applications.

We can also create our own apps here.
Lets we create our app with command

```bash
python manage.py startapp playground
```

Everytime you create an app, you need to register the app in settings

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'playground'
]
```

### views

Open the playground app, there is a views.py file
A view function is a function that takes request and returns a response.
It is a request handler handler, in some frameworks it is called action.
Actulally view is not the UI that user can see, that part is template in django
These are just request handlers or actions they are not the actual views.

- Open the playground app, and you'll find a views.py file.
- A view function is responsible for handling requests and returning responses. In some frameworks, it is referred to as an action.
- A "view" is not what the user sees—that part is done by Django templates.
- These functions just handle requests; they don't create what the user sees.

### template

- Is the actual HTML returned to the client

## Data Model

Each app can have its own data model
