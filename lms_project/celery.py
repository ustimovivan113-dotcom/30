import os
from celery import Celery

# Указываем Django, где брать настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms_project.settings')

app = Celery('lms_project')

# Загружаем все настройки с префиксом CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически ищем задачи во всех приложениях
app.autodiscover_tasks()