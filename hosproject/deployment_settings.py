import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

# ✅ Use .get() instead of []
ALLOWED_HOSTS = [os.environ.get("RENDER_EXTERNAL_HOSTNAME", "backend-cs8c.onrender.com")]

# ✅ Fix CSRF trusted origins (must be a list, and https:// is required for Render)
CSRF_TRUSTED_ORIGINS = [
    f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'backend-cs8c.onrender.com')}"
]

DEBUG =False
SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-key")

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


CORS_ALLOWED_ORIGINS = [
    "https://frontend-miux.onrender.com",
]


STORAGES = {
    "default":{
        "BACKEND" : "django.core.files.storage.filesystemstorage",
    },
    "staticfiles":{
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage", 
    },
}

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),  # safe lookup
        conn_max_age=600,
    )
}