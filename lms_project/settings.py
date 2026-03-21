"""
Django settings for lms_project project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-abc123secretkey456fordevonly789'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # third party
    'rest_framework',
    
    # local apps
    'users',
    'lms',
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

ROOT_URLCONF = 'lms_project.urls'

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

WSGI_APPLICATION = 'lms_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'users.User'

# ==================== Stripe и dotenv ====================
import os
from dotenv import load_dotenv

load_dotenv()  # загружает .env автоматически

STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

if not STRIPE_SECRET_KEY:
    print("⚠️  STRIPE_SECRET_KEY не найден в .env файле!")
    print("Создайте файл .env в корне проекта и добавьте строку:")
    print("STRIPE_SECRET_KEY=sk_test_ваш_ключ")

# ==================== drf-yasg (Swagger) ====================
INSTALLED_APPS += ['drf_yasg']

# ==================== Celery + Celery Beat ====================
# Redis (broker и backend результатов)
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Сериализаторы (json — самый безопасный и быстрый)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Часовой пояс — ОБЯЗАТЕЛЬНО совпадает с TIME_ZONE в проекте
CELERY_TIMEZONE = 'Europe/Moscow'

# Результаты задач храним максимум сутки
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

# Подключаем django-celery-beat (расписание хранится в базе данных)
INSTALLED_APPS += ['django_celery_beat']

# Импортируем crontab — ЭТО КЛЮЧЕВОЕ ИСПРАВЛЕНИЕ
from celery.schedules import crontab

# Расписание периодических задач
CELERY_BEAT_SCHEDULE = {
    'block-inactive-users-every-day': {
        'task': 'lms.tasks.block_inactive_users',
        'schedule': crontab(hour=3, minute=0),  # каждый день в 03:00 ночи
        'args': (),
    },
}