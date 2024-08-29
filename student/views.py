from django.shortcuts import render

from student.models import Student


def your_student(request):
    data = Student.objects.all()
    return render(request, 'student/student.html', {'data': data})
