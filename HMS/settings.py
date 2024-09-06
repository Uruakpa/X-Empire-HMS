"""
Django settings for HMS project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'on9*bf65je3#4+jphqufropk!s9*i&$*54@_9t8^6+c)iro2&q'
# SECRET_KEY = os.environ.get('SECRET_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVrbXZ6Z3hueGlteHJ3dGx1dmxqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU1NTY2NTksImV4cCI6MjA0MTEzMjY1OX0.wyA_aBpGBJsTdIg38q0VMVX7CakVW1XhDAwQOR2DiDU')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['x-empire-hms.onrender.com','127.0.0.1', 'localhost']
# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(",")
# SUPABASE_DB_URL = os.environ.get("SUPABASE_DB_URL")
# DJANGO_ENV = os.environ.get('DJANGO_ENV')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third part
    'phonenumber_field',

    # own
    'hotel',
    'accounts',
    'account',
    'Admin',
    'frontdesk',
    'guest',
    'room',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'HMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'HMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        # 'USER': os.environ.get('DB_USER'),
        # 'PASSWORD': os.environ.get('DB_USER_PASSWORD'),
        # 'HOST': os.environ.get('DB_HOST'),
        # 'PORT'
    }
}
# Check if the Supabase database URL is set
# if SUPABASE_DB_URL:
#     # Use the Supabase database configuration
#     DATABASES = {
#         "default": dj_database_url.config(
#             default=SUPABASE_DB_URL, conn_max_age=600
#         )
#     }
# else:
#     # Use the SQLite database configuration for development
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# mail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your_email_address'
# EMAIL_HOST_PASSWORD = 'your_email_address_password'


# supabase database key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVrbXZ6Z3hueGlteHJ3dGx1dmxqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU1NTY2NTksImV4cCI6MjA0MTEzMjY1OX0.wyA_aBpGBJsTdIg38q0VMVX7CakVW1XhDAwQOR2DiDU;