from django.urls import path, include
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.StudentListView.as_view(), name='home'),
    path('create/', views.StudentCreateView.as_view(), name='student-create'),
    path('<int:pk>/update', views.StudentUpdateView.as_view(), name='student-update'),
    path('<int:pk>/detail', views.StudentDetailView.as_view(), name='student-detail'),
    path('<int:student_id>/grade', views.AssignGradeView.as_view(), name='student-grade'),
    path('<int:student_id>/edit_grade', views.EditGradesView.as_view(), name='student-edit_grade'),
    path('<int:pk>/delete', views.delete_student, name='student-delete'),

]