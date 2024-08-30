from django import forms

from student.models import Student


# Форма отображения изменяемых данных.
class EditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['password', 'nickname_tg', 'nickname_inst']
