"""
WSGI config for background_remover project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "config.settings.local"
)

#now lets use settings.common instead of production

application = get_wsgi_application()

#app = application #This is needed because of vercel