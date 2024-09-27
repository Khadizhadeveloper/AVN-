from django.urls import path
from .views import StudentListAPIView, StudentCreateAPIView, StudentDetailAPIView, StudentUpdateAPIView, StudentDeleteAPIView

app_name = 'api'


urlpatterns = [
    path('', StudentListAPIView.as_view(), name='student'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='detail_student'),
    path('create/', StudentCreateAPIView.as_view(), name='create_student'),
    path('update/<int:pk>/', StudentUpdateAPIView.as_view(), name='update_student'),
    path('delete/<int:pk>/', StudentDeleteAPIView.as_view(), name='delete_student'),
]