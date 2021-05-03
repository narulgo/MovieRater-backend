"""
ASGI config for movierater project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
>>>>>>> 3afca6c2a2eb7b733f6b361c20c76d681fc4aa85
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movierater.settings')

application = get_asgi_application()
