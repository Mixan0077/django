from django.db import models
from django.urls import reverse


class Izdelie(models.Model):
    izdelie = models.CharField('Изделие', max_length=20)

    def __str__(self):
        return self.izdelie

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'


class Products(models.Model):
    name = models.CharField('Наименование', max_length=20)
    description = models.TextField('Описание')
    izdelie = models.ForeignKey('Izdelie', blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField('Количество')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('description', kwargs={'products_id': self.pk})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Client(models.Model):
    phone = models.CharField('Телефон', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

