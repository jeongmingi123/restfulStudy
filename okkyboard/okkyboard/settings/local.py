from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgres',
        'NAME': 'impactstation1',
        'USER': 'impactstation',
        'PASSWORD': 'save2020!',
        'HOST': 'localhost',
        'POST': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", # strict mode 설정 추가
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restfulstudy',
        'USER': 'restfulstudy',
        'PASSWORD': 'restfulstudy',
        'HOST': 'localhost',
        'POST': '5432',
    }
}

DEBUG = True

ALLOWED_HOSTS = ['localhost', '192.168.0.1']

INSTALLED_APPS += [
    'django_extensions',
]
