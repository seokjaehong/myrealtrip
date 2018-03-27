
import json
import os

import raven

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)

AUTH_USER_MODEL ='members.user'
# Static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]

# secrets
SECRETS_DIR = os.path.join(ROOT_DIR, '.secrets')
SECRETS_BASE = os.path.join(SECRETS_DIR, 'base.json')
SECRETS_LOCAL = os.path.join(SECRETS_DIR, 'local.json')
SECRETS_DEV = os.path.join(SECRETS_DIR, 'dev.json')
SECRETS_PRODUCTION = os.path.join(SECRETS_DIR, 'production.json')
secrets_base = json.loads(open(SECRETS_BASE, 'rt').read())

#Django secret key
SECRET_KEY = secrets_base['SECRET_KEY']

# AWS
AWS_ACCESS_KEY_ID = secrets_base['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets_base['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets_base['AWS_STORAGE_BUCKET_NAME']
# AWS_S3_ENDPOINT_URL ='http://s3.ap-northeast-2.amazonaws.com'
AWS_DEFAULT_ACL = 'private'
AWS_S3_REGION_NAME = 'ap-northeast-2'
AWS_S3_SIGNATURE_VERSION='s3v4'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'django_extensions',
    'photos',
    'storages',
    'members',
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

ROOT_URLCONF = 'config.urls'

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Raven
RAVEN_CONFIG = {
    'dsn': secrets_base['RAVEN_DSN'],
    'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}