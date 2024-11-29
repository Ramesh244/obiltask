# Django Multi-Tenant Application

This Django-based application provides a solution for managing multiple tenants using a shared schema model. 
Each tenant has its own data, but they all share the same database schema, making it easier to manage and scale while keeping things simple.

## Features

- Multi-tenant architecture with a shared schema model.
- Tenant-specific data for each user, including CRUD operations for tasks.
- Built-in rate-limiting using Redis for API endpoints.
- A simple UI for adding and viewing tasks for each tenant.
- Supports Django Rest Framework (DRF) for API integration.

## Installation

### Prerequisites
- Python 3.11
- Django 5.1.
- Redis (for caching and rate-limiting)

### Steps to Get Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ramesh244/obiltask/tree/master.git


2. Navigate That path

3. create vituval envirnment
     python -m venv envname
     ./envname/Scripts/activate
4. In stall requirmemts
    pip install -r requirements.txt
5 .Set up your database:
    Make sure your database is set up correctly, then run the migrations to create the required tables for the multi-tenant model.
6. apply Makemigratipons and migrate then run it 

