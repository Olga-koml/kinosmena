from pathlib import Path
import os

from dotenv import load_dotenv
from corsheaders.defaults import default_headers



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ital(1(gpoy7*7%781ysi*go&pj)+(y0#a+9hyi9+=28lk3wl@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

FORCE_SCRIPT_NAME = '/kinosmena'

# CSRF_TRUSTED_ORIGINS = [
#     'https://*rbychin.ddns.net/',
#     'https://*.127.0.0.1',
#     'http://*rbychin.ddns.net/',
#     'http://*.127.0.0.1',
#     'https://kinosmena.vercel.app/'
# ]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'django_filters',

    'users.apps.UsersConfig',
    'projects.apps.ProjectsConfig',
    'shifts.apps.ShiftsConfig',
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
    'users.middleware.GetOrCreateUser',
]


ROOT_URLCONF = 'kinosmena_backend.urls'

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

WSGI_APPLICATION = 'kinosmena_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

# TIME_ZONE = 'Europe/Moscow'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
# STATIC_URL = 'kinosmena/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = Path(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

# SESSION_COOKIE_SECURE = True
CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = [
#     'https://kinosmena.vercel.app/',
# ]

CORS_ALLOW_HEADERS = default_headers + (
    'Access-Control-Allow-Origin',
    'ngrok-skip-browser-warning',
    'Access-Control-Allow-Credentials',
)
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {  # авторизация в джанго по токену
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Use your token in the following format: <strong>Token <em>&lt;your-token&gt;</em></strong> ',
        },

        # 'Basic': {'type': 'basic'},  # базова авторизация
    },
    'USE_SESSION_AUTH': True,  # кнопка джанго логин можно отключить поменяв False
    'JSON_EDITOR': True,
    'SHOW_REQUEST_HEADERS': True,
    'DEFAULT_MODEL_RENDERING': 'model',  # Отображение моделей (model, example)
    # Глубина отображения моделей (-1 - без ограничений)
    'DEFAULT_MODEL_DEPTH': 2,
    'DOC_EXPANSION': 'list',  # full, none
    'OPERATIONS_SORTER': 'alpha',  # Сортировка операций (alpha, method)
    'TAGS_SORTER': 'alpha',  # Сортировка тегов (alpha, order)
}

# Constants
MAX_LEN_NAME = 20
MAX_LEN_DESCRIPTION = 50
MESSAGE_TEXT_REGEX_VALID = 'Недопустимые символы'
MESSAGE_MAX_LEN_NAME_VALID = f'Не более {MAX_LEN_NAME} символов'
MESSAGE_MAX_LEN_DESCRIPTION_VALID = f'Не более {MAX_LEN_DESCRIPTION} символов'

MAX_HOURS = 24
MIN_HOURS = 1
MESSAGE_MIN_HOURS_VALID = f'Значение не менее {MIN_HOURS}'
MESSAGE_MAX_HOURS_VALID = f'Значение не более {MAX_HOURS}'
# MESSAGE_HOURS_SHIFT_DURATION_VALID = f'Недопустимое значение.Возможны значения от {MIN_HOURS_SHIFT_DURATION} до {MAX_HOURS_SHIFT_DURATION}'
DEFAULT_HOURS_DURATION = 8

MIN_VALUE_RATE = 0
MAX_VALUE_RATE = 999999
MAX_VALUE_SHIFT_RATE = 999999999
MESSAGE_MIN_VALUE_RATE_VALID = f'значение не меньше {MIN_VALUE_RATE}'
MESSAGE_MAX_VALUE_RATE_VALID = f'значение не более {MAX_VALUE_RATE}'
MESSAGE_MAX_VALUE_SHIFT_RATE_VALID = f'значение не более {MAX_VALUE_SHIFT_RATE}'

# MESSAGE_VALUE_RATE_VALID = f'Допустимое значение стоимости от {MIN_VALUE_RATE} до {MAX_VALUE_RATE}'
# MESSAGE_VALUE_SHIFT_RATE_VALID = f'Допустимое значение стоимости от {MIN_VALUE_RATE} до {MAX_VALUE_SHIFT_RATE}'

BOT_TOKEN = os.getenv('BOT_TOKEN')
