from django.test import TestCase
from lms.models import Course

class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            name="Тестовый курс",
            description="Описание тестового курса",
            price=1000
        )
        self.assertEqual(course.name, "Тестовый курс")
        self.assertEqual(course.price, 1000)