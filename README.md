## Деплой на продакшн-сервер

Проект автоматически деплоится на VPS при каждом push в ветку `develop`.

### Ручной запуск на сервере (если нужно)
```bash
cd /home/deploy/lms
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn