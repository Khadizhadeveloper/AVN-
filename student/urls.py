from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.all_students, name='home'),
    path('create/', views.create_student, name='student-create'),
    path('<int:pk>/update', views.update_student, name='student-update'),
    path('<int:pk>/delete', views.delete_student, name='student-delete'),

]