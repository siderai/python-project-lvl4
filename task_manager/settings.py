import os

from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

# SECRET_KEY='django-insecure-ng$@(dmo))my_%@-4-65pi*kiixsmiz^a(v+@df!!(d(!=2+(l'
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True
# DEBUG = os.getenv('DEBUG', False) == 'True'

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = [
    "127.0.0.1",
    'localhost',
    "webserver",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "debug_toolbar",
    "task_manager",
    "task_manager.tasks",
    "task_manager.users",
    "task_manager.statuses",
    "task_manager.labels",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "task_manager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "task_manager/templates"),
            os.path.join(BASE_DIR, "task_manager/templates/users"),
            os.path.join(BASE_DIR, "task_manager/templates/tasks"),
            os.path.join(BASE_DIR, "task_manager/templates/labels"),
            os.path.join(BASE_DIR, "task_manager/templates/statuses"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "task_manager.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# def show_toolbar(request):
#     return True

# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_TOOLBAR_CALLBACK": show_toolbar,
# }

LOGIN_URL = '/login/'

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "UTC"
DATETIME_FORMAT = "d-m-Y H:i"
USE_I18N = True
USE_L10N = False
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
