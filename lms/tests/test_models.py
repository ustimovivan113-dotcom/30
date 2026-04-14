from django.test import TestCase
from lms.models import Course, Lesson

class CourseModelTest(TestCase):
    """Тесты для модели Course"""

    def test_course_creation(self):
        """Проверяем, что курс можно создать"""
        course = Course.objects.create(
            name="Тестовый курс по Python",
            description="Описание тестового курса",
            price=1500
        )
        self.assertEqual(course.name, "Тестовый курс по Python")
        self.assertEqual(course.price, 1500)
        self.assertTrue(course.id is not None)

    def test_course_str_method(self):
        """Проверяем метод __str__ у Course"""
        course = Course.objects.create(name="Django для начинающих", description="...", price=0)
        self.assertEqual(str(course), "Django для начинающих")


class LessonModelTest(TestCase):
    """Тесты для модели Lesson"""

    def setUp(self):
        self.course = Course.objects.create(
            name="Основной курс",
            description="Тестовый курс",
            price=1000
        )

    def test_lesson_creation(self):
        """Проверяем создание урока"""
        lesson = Lesson.objects.create(
            name="Урок 1: Введение",
            description="Описание урока",
            course=self.course
        )
        self.assertEqual(lesson.name, "Урок 1: Введение")
        self.assertEqual(lesson.course, self.course)