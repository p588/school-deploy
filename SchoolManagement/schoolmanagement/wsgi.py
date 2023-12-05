"""
WSGI config for schoolmanagement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

settings_module = 'azure_project.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'schoolmanagement.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolmanagement.settings')

application = get_wsgi_application()

application=get_wsgi_application()
