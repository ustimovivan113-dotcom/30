from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

from .models import Course, Payment
from django.contrib.auth import get_user_model


@shared_task
def send_course_update_email(course_id):
    """
    Асинхронная рассылка письма подписчикам курса об обновлении материалов
    """
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return

    # Получаем email всех, кто оплатил курс (можно заменить на другую логику подписки)
    paid_users_emails = Payment.objects.filter(
        course=course,
        status='paid'
    ).values_list('user__email', flat=True).distinct()

    if not paid_users_emails:
        return

    subject = f"Обновление материалов в курсе: {course.name}"
    message = (
        f"В курсе '{course.name}' появились новые материалы или изменения.\n\n"
        f"Проверьте обновления здесь: http://127.0.0.1:8000/courses/{course.id}/\n"
        f"С уважением,\nКоманда LMS"
    )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=paid_users_emails,
        fail_silently=False,
    )


@shared_task
def block_inactive_users():
    """
    Блокирует пользователей, не заходивших более 30 дней
    Запускается раз в сутки через Celery Beat
    """
    month_ago = timezone.now() - timedelta(days=30)
    User = get_user_model()

    inactive_users = User.objects.filter(
        last_login__lt=month_ago,
        is_active=True,
        is_staff=False,
        is_superuser=False
    )

    count = inactive_users.update(is_active=False)
    print(f"[block_inactive_users] Заблокировано {count} пользователей")