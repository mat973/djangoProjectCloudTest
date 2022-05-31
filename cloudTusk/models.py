from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Tusk(models.Model):
    variable = models.IntegerField('Вариант',unique=True,primary_key=True)
    text = models.TextField('Основной текст задания',default='text zadania')
  #  date = models.DateTimeField('Дата', default=timezone.now)

    def __str__(self):
        return f'Вариант задания номер: {self.variable}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def get_absolute_url(self):
        return reverse('tusk')


class UserTask(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_tusk')
    number = models.PositiveSmallIntegerField()


class SubmitAnswer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    variable = models.IntegerField()
    text = models.SlugField()
    answer =models.TextField(default='text')
