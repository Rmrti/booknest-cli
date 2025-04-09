# BookNest CLI

A CLI app for managing a mini book rental system.
# 📚 BookNest CLI

BookNest is a command-line application for managing book rentals using Python, SQLAlchemy, and Alembic.

## Features
- View all books and customers
- Rent and return books
- View active rentals

## Setup
```bash
pipenv install
pipenv shell
alembic init lib/db/migrations
alembic revision --autogenerate -m "Initial"
alembic upgrade head
python lib/db/seed.py
python lib/cli.py
