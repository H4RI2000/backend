"""
ASGI config for hosproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

settigs_module = 'hosproject.deployment_settings' if 'HOSTNAME' in os.environ else 'hosproject.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hosproject.settings')

application = get_asgi_application()
