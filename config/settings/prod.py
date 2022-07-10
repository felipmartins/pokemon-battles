import django_on_heroku
from decouple import config

from .base import *


SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'site'
]

django_on_heroku.settings(locals(), staticfiles=False)
