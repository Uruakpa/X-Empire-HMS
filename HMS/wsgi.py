"""
WSGI config for HMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HMS.settings')

# application = get_wsgi_application()
if os.environ.get('DJANGO_ENV') == 'production':
    app = get_wsgi_application()
else:
    application = get_wsgi_application()
