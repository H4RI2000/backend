import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ.get['hostname']]
CSRF_TRUSTED_ORIGINS = ['http://'+os.environ.get['hostname']]


DEBUG =False
SECRET_KEY = os.environ.get['SECRET_KEY']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware", 
]


#CORS_ALLOWED_ORIGINS = [
 #   "http://localhost:5173",
#]


STORAGES = {
    "default":{
        "BACKEND" : "django.core.files.storage.filesystemstorage",
    },
    "staticfiles":{
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage", 
    },
}

DATABASES ={
    'default': dj_database_url.config(
        default = os.environ['DATABASE_URL'],
        conn_max_age = 600
        

    )
}