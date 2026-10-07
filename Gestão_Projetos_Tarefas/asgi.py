"""
ASGI config for Gestão_Projetos_Tarefas project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gestão_Projetos_Tarefas.settings')

application = get_asgi_application()
