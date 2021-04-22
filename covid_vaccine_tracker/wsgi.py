import os

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise 
from whitenoise import WhiteNoise
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'covid_vaccine_tracker.settings')

application = get_wsgi_application()
application = WhiteNoise(application)
