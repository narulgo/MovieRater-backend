from pathlib import Path

<<<<<<< HEAD

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-x%gl-9wn)i^#h#(&v=r$)#blp84f6@(z_e7k7ih$3-g*$okd+c'
=======
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = '6v3q1ofg6-$pcl4_v*s@wrlycyke-_jjq^c-z+#l#-!5#f_1+w'
>>>>>>> 3afca6c2a2eb7b733f6b361c20c76d681fc4aa85

DEBUG = True

ALLOWED_HOSTS = []


<<<<<<< HEAD
=======

>>>>>>> 3afca6c2a2eb7b733f6b361c20c76d681fc4aa85
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
<<<<<<< HEAD
    'rest_auth',
    'rest_auth.registration',
=======
>>>>>>> 3afca6c2a2eb7b733f6b361c20c76d681fc4aa85
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080"
]

ROOT_URLCONF = 'movierater.urls'

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

WSGI_APPLICATION = 'movierater.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

<<<<<<< HEAD

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}


=======
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': {
        'rest_framework.permissions.IsAuthenticated',
    }
}

>>>>>>> 3afca6c2a2eb7b733f6b361c20c76d681fc4aa85
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


<<<<<<< HEAD
=======

>>>>>>> 3afca6c2a2eb7b733f6b361c20c76d681fc4aa85
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
<<<<<<< HEAD

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======
>>>>>>> 3afca6c2a2eb7b733f6b361c20c76d681fc4aa85
