from django.urls import path, include

from student.views import your_student, edit_student

urlpatterns = [
    path('student/', your_student, name='student'),  # Отображения данных студента.
    path('edit/<int:student_id>/', edit_student, name='edit_student'),  # Для изменения данных.
]
