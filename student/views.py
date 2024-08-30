from django.shortcuts import render, get_object_or_404, redirect

from student.forms import EditForm
from student.models import Student


# Отображение данных студента.
def your_student(request):
    data = Student.objects.all()
    return render(request, 'student/student.html', {'data': data})


# Изменение данных студента.
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')  # Перенаправление на другую страницу, после изменений данных.
    else:
        form = EditForm(instance=student)
    return render(request, 'student/edit_student.html', {'form': form})
