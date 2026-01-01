"""
WSGI config for fastCopyConfig project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fastCopyConfig.settings')

<<<<<<< HEAD
application = get_wsgi_application()
=======
application = get_wsgi_application()
>>>>>>> 0afc99f50d603d22b0140b559ce2a9a6385d4fa6
