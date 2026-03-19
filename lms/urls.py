from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonListCreateView, LessonRetrieveUpdateDestroyView, CreatePaymentView

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-detail'),
    path('payments/', CreatePaymentView.as_view(), name='payment-create'),
]

urlpatterns += router.urls