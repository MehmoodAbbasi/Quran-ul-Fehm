import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'QURAN_UL_EMAN' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QURAN_UL_EMAN.settings')

application = get_wsgi_application()
