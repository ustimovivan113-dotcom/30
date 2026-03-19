from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField('Название', max_length=255)
    preview = models.ImageField('Превью', upload_to='courses/previews/', blank=True, null=True)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена в рублях', default=0)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    preview = models.ImageField('Превью', upload_to='lessons/previews/', blank=True, null=True)
    video_link = models.URLField('Ссылка на видео', blank=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons'
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['id']

    def __str__(self):
        return f"{self.course.name} — {self.name}"


class Payment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='payments'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_price_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)
    payment_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=50, default='created')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
        ordering = ['-created_at']

    def __str__(self):
        return f"Платёж {self.id} — {self.course.name}"