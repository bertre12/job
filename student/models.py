from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    image = models.ImageField(upload_to='static/images/', null=True, verbose_name='Фото')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    phone = models.CharField(max_length=255, verbose_name='№ телефона')
    e_mail = models.EmailField(max_length=255, verbose_name='Электронная почта')
    nickname_tg = models.CharField(max_length=255, null=True, verbose_name='Никнейм Telegram')
    nickname_inst = models.CharField(max_length=255, null=True, verbose_name='Никнейм Instagram')
    group_number = models.CharField(max_length=255, verbose_name='№ группы')
    number_of_points = models.IntegerField(max_length=100, default=0, verbose_name='Количество баллов')
    status = models.CharField(max_length=100, verbose_name='Статус')
    package = models.CharField(max_length=255, verbose_name='Пакет')
    internship = models.CharField(max_length=255, verbose_name='Стажировка')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.name
