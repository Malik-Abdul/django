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
