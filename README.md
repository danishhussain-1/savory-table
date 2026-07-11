# Savory Table — Fine Dining Restaurant Web Platform

A premium, full-stack restaurant website built with **Django 5**, featuring a
dark elegant theme, online table reservations, dynamic menu management,
customer reviews, a photo gallery, and full user/admin dashboards.

## Tech Stack
- Backend: Django 5 (Python 3.12)
- Frontend: HTML5, CSS3 (Vanilla), Vanilla JavaScript
- Database: SQLite (development)
- Deployment: PythonAnywhere

## Apps
| App | Responsibility |
|---|---|
| `core` | Home page, About, Contact form, Newsletter signup |
| `accounts` | Authentication, user profile, user dashboard |
| `menu` | Menu categories & items, search, category filtering |
| `reservations` | Table booking system |
| `reviews` | Customer reviews & ratings |
| `gallery` | Restaurant photo gallery with category filters |

## Local Setup
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Project Status
🚧 Under active development — built step by step as a portfolio showcase.