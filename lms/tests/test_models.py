from django.test import TestCase
from django.apps import apps

from lms.models import Course, Lesson


class CourseModelTest(TestCase):
    """Тесты для модели Course"""

    def test_course_creation(self):
        course = Course.objects.create(
            name="Тестовый курс",
            description="Описание курса для теста",
            price=999
        )
        self.assertEqual(course.name, "Тестовый курс")
        self.assertEqual(course.price, 999)
        self.assertIsNotNone(course.pk)

    def test_course_str(self):
        course = Course.objects.create(name="Python Advanced", description="...", price=0)
        self.assertEqual(str(course), "Python Advanced")


class LessonModelTest(TestCase):
    """Тесты для модели Lesson"""

    def setUp(self):
        # Явно проверяем, что приложения загружены
        self.assertTrue(apps.is_installed('lms'))
        self.course = Course.objects.create(
            name="Базовый курс",
            description="Для тестов уроков",
            price=500
        )

    def test_lesson_creation(self):
        lesson = Lesson.objects.create(
            name="Урок №1",
            description="Тестовый урок",
            course=self.course
        )
        self.assertEqual(lesson.name, "Урок №1")
        self.assertEqual(lesson.course_id, self.course.id)