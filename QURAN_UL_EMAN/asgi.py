"""
ASGI config for QURAN_UL_EMAN project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QURAN_UL_EMAN.settings')

application = get_asgi_application()

# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import main_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QURAN_UL_EMAN.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            main_app.routing.websocket_urlpatterns
        )
    ),
})
