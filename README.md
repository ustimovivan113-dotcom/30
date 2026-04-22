# LMS Project (Containerized)

Проект системы управления обучением (LMS), упакованный в Docker с настроенным CI/CD.

## Стек технологий
- **Backend:** Django, DRF
- **Database:** PostgreSQL
- **Task Queue:** Celery, Redis
- **Web Server:** Nginx
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions

## Адрес проекта (Deployment)
Приложение доступно по адресу: [http://111.88.157.110](http://111.88.157.110)

## Как запустить локально

1. Клонируйте репозиторий.
2. Создайте файл `.env` в корне проекта и заполните его по примеру:
   ```env
   DEBUG=True
   SECRET_KEY=your_key
   POSTGRES_DB=lms_db
   POSTGRES_USER=lms_user
   POSTGRES_PASSWORD=lms_password
   DB_HOST=db
   DB_PORT=5432
   REDIS_HOST=redis
   REDIS_PORT=6379
   STRIPE_SECRET_KEY=sk_test_...