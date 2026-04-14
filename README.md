## 🚀 Деплой и CI/CD

### GitHub Actions Workflow
Проект использует GitHub Actions для автоматического:
- Запуска тестов при каждом push/pull request
- Автоматического деплоя на удалённый сервер (только из веток `develop` и `main`)

Workflow файл: `.github/workflows/deploy.yml`

### Настройка сервера (для проверяющего)

1. На сервере (Ubuntu 22.04/24.04) должен быть создан пользователь `deploy`
2. Установлены: `nginx`, `gunicorn`, `git`
3. Настроен systemd-сервис `gunicorn.service`
4. Настроен сайт в nginx
5. Добавлены Secrets в GitHub:
   - `VPS_HOST` — IP адрес сервера
   - `VPS_USER` — `deploy`
   - `VPS_SSH_KEY` — приватный SSH ключ

### Как запустить деплой
Просто сделайте push в ветку `develop` или `main` — после успешных тестов проект автоматически развернётся на сервере.

### Локальный запуск
```bash
python manage.py runserver