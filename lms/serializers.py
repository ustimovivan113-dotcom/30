from rest_framework import serializers
from .models import Course, Lesson, Payment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'preview', 'description', 'price']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'preview', 'video_link', 'course']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'course', 'payment_url', 'status', 'created_at']
        read_only_fields = ['payment_url', 'status', 'created_at']