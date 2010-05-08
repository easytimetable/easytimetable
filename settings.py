import os.path
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'db.sql'

# not needed for sqlite3
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''  
DATABASE_PORT = ''

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
SITE_ID = 1

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'staticfiles')
SERVE_STATIC_FILES = DEBUG
MEDIA_URL = '/site_media/'
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#6@1aqvb+=sk7=kgzi$(zws=wka5f&l^kff)3wdg&l3(74$kmx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'easytimetable.urls'

TEMPLATE_DIRS = ( 
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    # django contribs
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',

    # django apps
    'django_extensions',

    # project specific apps
    'agenda', 
)

# if a local_settings.py file exists, override current settings with those
# present in it.
try:
    from local_settings import *
except ImportError:
    pass
