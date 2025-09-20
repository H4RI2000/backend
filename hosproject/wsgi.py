"""
WSGI config for hosproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settigs_module = 'hosproject.deployment_settings' if 'HOSTNAME' in os.environ else 'hosproject.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hosproject.settings')
application = get_wsgi_application()
