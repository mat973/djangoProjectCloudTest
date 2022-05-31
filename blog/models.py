from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class News(models.Model):
    title = models.CharField('Название статьи', max_length=100,unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата',default=timezone.now)
    avtor = models.ForeignKey(User,verbose_name='Автор' ,on_delete=models.CASCADE)

    # views =models.IntegerField('Просмотры',default=1)
    # sizes = (
    #     ('S','Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    #     ('XL', 'X large')
    # )
    # shop_size = models.CharField(max_length=2, choices=sizes, default='S')

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return f'Новость:{self.title}'
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новость'




# class Task(models.Model):
#     pass
#
#
# class Variant(models.Model):
#     number = models.IntegerField(primary_key=True)
#     task = models.ForeignKey(Task,on_delete=models.CASCADE)
#     text = models.TextField(help_text='Текст')
#
#
# class Additional(models.Model):
#     variant = models.ForeignKey(Variant,on_delete=models.CASCADE)
#     file = models.FileField()
#
#
# class Dispersion(models.Model):
#     task =models.ForeignKey(Task,on_delete=models.CASCADE)
#     variant_number = models.IntegerField
#     first_name= models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#
