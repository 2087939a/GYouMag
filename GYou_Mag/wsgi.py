import os

 
from django.core.wsgi import get_wsgi_application

 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GYou_Mag.settings")
# IMPORT THE DJANGO SETUP - NEW TO 1.7


application = get_wsgi_application()