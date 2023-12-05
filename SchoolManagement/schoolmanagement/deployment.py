import os
from .settings import *
from .settings import BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['secret']

ALLOWED_HOSTS=[os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS=['http://'+os.environ['WEDSITE_HOSTNAME']]
DEBUG=False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')


connection_string=os.environ['AZURE_POSTGRESQL_CONNECTIONSSTRING']
parameters={pair.split('='):pair.split('=')[1] for pair in connection_string.split(' ')}
DATABASES= {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME':parameters['dbname'],
        'HOST':parameters['host'],
        'USER':parameters['user'],
        'PASSWORD':parameters['password'],
}
}
