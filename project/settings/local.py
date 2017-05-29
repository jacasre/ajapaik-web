# coding=utf-8
import sys
import os

from .default import *

print('LOCALPY')

DEBUG = True

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'ajapaik',
        'USER': 'misha',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    }
}

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'an*r-w2igycw-bdujbxg=$8n*9#d1o%bcb=xu1x(5=*doy+z6p'

ADMINS = (
    ('Name Surname', 'admin@example.com'),
)

MANAGERS = ADMINS

GOOGLE_ANALYTICS_KEY = 'waasmasdmaskdmkasdmaskdmaspd'
GOOGLE_API_KEY = 'waasmasdmaskdmkasdmaskdmaspd'

FLICKR_API_KEY = '22c88e7b04621344e8d3d54cc6f425a0'
FLICKR_API_SECRET = '14d76c62af2c82d9'

GOOGLE_PLUS_OAUTH2_CALLBACK_URL = '/'
GOOGLE_CLIENT_ID = 'saasdmkasndoaisdniad'

FACEBOOK_APP_KEY = ''
FACEBOOK_APP_SECRET = ''

TIME_ZONE = 'Europe/Helsinki'
LANGUAGE_CODE = 'ru'
