from django.urls import path, include

from student.views import your_student

urlpatterns = [
    path('student/', your_student, name='student'),
]
