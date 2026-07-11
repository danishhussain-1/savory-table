"""
WSGI config for the Savory Table project.

Exposes the WSGI callable as a module-level variable named ``application``.
Used by PythonAnywhere and other traditional WSGI hosts in production.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'savory_table.settings')

application = get_wsgi_application()