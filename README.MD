# Refund Manager Tool

A small internal tool built. This will help a support team manage customer refund requests - create them, view all of them, filter by status, and update a request's status.

## Tech Stack
- Python / Django
- SQLite (Django's default database, didn't need anything more for this scope)
- Django Templates + Bootstrap 5 (styled using Regent's brand colors)

## What it does
- Create a refund request
- View all refund requests
- Filter refund requests by status (Pending, Approved, Rejected, Refunded)
- Update the status of a refund request

## Before You Start

You'll need Python 3.10+ installed. Check by running `python --version` in your terminal. If you don't have it, grab it from https://www.python.org/downloads/

## How to Run This Locally

**1. Clone the repo and go inside the folder**
```
git clone https://github.com/KuyaSei/refund_tool_regent
cd aj-refund-tool
```

**2. Create a virtual environment**

This keeps the project's dependencies separate from anything else on your machine.
```
python -m venv venv
```

**3. Activate the virtual environment**

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

You'll know it worked if you see `(venv)` show up at the start of your terminal line.

**4. Install the required packages**
```
pip install -r requirements.txt
```

**5. Run the database migrations**

This sets up the database tables the app needs.
```
python manage.py migrate
```

**6. (Optional) Create a superuser**

Only needed if you want to check out the Django admin panel too.
```
python manage.py createsuperuser
```

It'll ask for a username, email (you can skip this), and password.

**7. Run the server**
```
python manage.py runserver
```

**8. Open it in your browser**
- Main app: http://127.0.0.1:8000/refunds/
- Django admin (if you made a superuser): http://127.0.0.1:8000/admin/

I left a few sample refund requests already in the database so the app isn't empty on first load - you should see the list and filters working right away.

