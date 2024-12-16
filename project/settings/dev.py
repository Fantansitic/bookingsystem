from .base import *

DEPLOY = 'DEV'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookingsystem',  
        'USER': 'scydydadmin',  
        'PASSWORD': 'yd123456yd',  
        'HOST': '127.0.0.1',  
        'PORT': '23306',  
        'TEST': {
            'NAME': 'bookingsystem-test', 
        }
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
INTERNAL_IPS = ['127.0.0.1', ]
ALLOWED_HOSTS = ['127.0.0.1',
                 '0.0.0.0',
                 ]
DJANGO_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'rest_framework',
    'requests',
    'django_filters',
    'debug_toolbar',
    'corsheaders',
]

LOCAL_APPS = [
    'booking.apps.BookingConfig',
    'account.apps.AccountConfig',
    'manager.apps.ManagerConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + LOCAL_APPS
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = (
    'AUTH-TOKEN',
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'user-agent',
    'accept-encoding',
    'Access-Control-Allow-Origin'
)