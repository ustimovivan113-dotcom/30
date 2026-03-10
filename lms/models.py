from django.db import models


class Course(models.Model):
    name = models.CharField('Название', max_length=255)
    preview = models.ImageField('Превью', upload_to='courses/previews/', blank=True, null=True)
    description = models.TextField('Описание')

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
        return '{} - {}'.format(self.course.name, self.name)
