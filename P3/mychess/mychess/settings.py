"""
Django settings for mychess project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from os import getenv
import os
from dotenv import load_dotenv
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-o76=!63^64b&_@!2k7=dt*j0m=%+jjmb9n-5mxl0h75qr#q7#k'
if 'RENDER' in os.environ:
    SECRET_KEY = os.environ.get('SECRET_KEY')
else:
    SECRET_KEY = os.environ.get('SECRET_KEY', default='santacg123')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
if 'DEBUG' in os.environ:
    DEBUG = os.environ.get('DEBUG').lower() in ['true', 't', '1']
else:
    DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['localhost']
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    'daphne',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'models',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mychess.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'mychess.wsgi.application'
ASGI_APPLICATION = 'mychess.asgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}

# Replace the DATABASES section of your settings.py with this
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'psi',
        'USER': 'alumnodb',
        'PASSWORD': 'alumnodb',
        'HOST': 'localhost',  # O una IP si es remota pero considerada 'local' para tus propósitos
        'PORT': '5432',
    },
    'neon': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('PGDATABASE'),
        'USER': getenv('PGUSER'),
        'PASSWORD': getenv('PGPASSWORD'),
        'HOST': getenv('PGHOST'),
        'PORT': getenv('PGPORT', 5432),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

LOCALPOSTGRES = 'postgresql://alumnodb:alumnodb@localhost:5432/psi'

if 'TESTING' in os.environ:
    databaseenv = dj_database_url.parse(LOCALPOSTGRES, conn_max_age=600)
else:
    databaseenv = dj_database_url.config(conn_max_age=600, default=LOCALPOSTGRES)

DATABASES['default'] = databaseenv
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',      
    )
}

AUTH_USER_MODEL = 'models.Player'
