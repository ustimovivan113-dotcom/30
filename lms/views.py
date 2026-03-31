from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .models import Course, Lesson, Payment
from .serializers import CourseSerializer, LessonSerializer, PaymentSerializer
from .services import create_payment


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class CreatePaymentView(generics.CreateAPIView):
    queryset = Payment.objects.none()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Создать платёж за курс. В body передайте {'course': <id_курса>}"
    )
    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course')
        if not course_id:
            raise ValidationError({"course": "Обязательно укажите ID курса"})

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise ValidationError({"course": "Курс не найден"})

        if course.price <= 0:
            raise ValidationError({"price": "У курса должна быть цена > 0"})

        payment = create_payment(course, user=request.user)

        serializer = self.get_serializer(payment)
        return Response(serializer.data, status=201)

    from lms.tasks import send_course_update_email

    class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Lesson.objects.all()
        serializer_class = LessonSerializer

        def perform_update(self, serializer):
            lesson = serializer.save()
            # После обновления урока — рассылаем уведомление подписчикам курса
            course_id = lesson.course.id
            send_course_update_email.delay(course_id)