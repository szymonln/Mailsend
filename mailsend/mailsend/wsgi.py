"""
WSGI config for mailsend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailsend.settings')

application = get_wsgi_application()
