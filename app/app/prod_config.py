import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
BASE_URL = 'http://127.0.0.1:8000/'
BASE_SITE_NAME = 'Retail App'

# Loading data form environment files.
SECRET_KEY = os.environ.get('SECRET_KEY')

# Allowed hosts that can access the app.
ALLOWED_HOSTS = ['*']

# How much time the password reset link expires.
PASSWORD_RESET_TIMEOUT = 900

# File upload and download size
DATA_UPLOAD_MAX_MEMORY_SIZE = 429916160  # 500 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 429916160  # 500 MB

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/usr/src/staticfiles'
MEDIA_ROOT = '/usr/src/mediafiles'

# Location of static files.

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
