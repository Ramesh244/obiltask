Django Multi-Tenant Task Manager
A Django-based application that demonstrates how to manage tasks for multiple tenants 
(e.g., organizations or users) within a shared schema database model. Each tenant can have its own tasks, 
which are logically isolated using tenant-specific filtering.

Features

Multi-Tenant Support: Manage tasks for different tenants while sharing a single database schema.
Task Management:
View tasks for a specific tenant.
Create new tasks for a specific tenant.
Class-Based Views: Efficiently handle task listing and creation with Django's ListView and CreateView.
Dynamic Templates: Tenant-specific task templates for viewing and adding tasks.

obil/
├── obilapp/                     # App for tenant and task management
│   ├── migrations/           # Database migrations
│   ├── admin.py              # Admin configurations
│   ├── apps.py               # App configuration
│   ├── models.py             # Models for Tenant and Task
│   ├── views.py              # Class-based views for task management
│   ├── urls.py               # App-specific URL patterns
│   └── tests.py              # Unit tests
├── obil/                  # Project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # Project-level URL configurations
│   └── wsgi.py               # WSGI entry point
├── templates/            # HTML templates
│   │       ├── task_list.html
│   │       └── task_form.html
├── db.sqlite3                # SQLite database (default)
├── manage.py                 # Django management script









