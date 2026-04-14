from django.test import TestCase
from django.conf import settings
from lms.models import Course, Lesson

class CourseModelTest(TestCase):
    """Тесты для модели Course"""

    def test_course_creation(self):
        """Проверяем создание курса"""
        course = Course.objects.create(
            name="Тестовый курс по Python",
            description="Описание тестового курса",
            price=1500
        )
        self.assertEqual(course.name, "Тестовый курс по Python")
        self.assertEqual(course.price, 1500)
        self.assertIsNotNone(course.id)

    def test_course_str_method(self):
        """Проверяем строковое представление курса"""
        course = Course.objects.create(
            name="Django для начинающих",
            description="Тест",
            price=2000
        )
        self.assertEqual(str(course), "Django для начинающих")


class LessonModelTest(TestCase):
    """Тесты для модели Lesson"""

    def setUp(self):
        """Создаём курс перед каждым тестом урока"""
        self.course = Course.objects.create(
            name="Основной курс",
            description="Тестовый курс для уроков",
            price=1000
        )

    def test_lesson_creation(self):
        """Проверяем создание урока"""
        lesson = Lesson.objects.create(
            name="Урок 1: Введение в Django",
            description="Описание первого урока",
            course=self.course,
            video_link="https://youtube.com/test"
        )
        self.assertEqual(lesson.name, "Урок 1: Введение в Django")
        self.assertEqual(lesson.course, self.course)
        self.assertIsNotNone(lesson.id)