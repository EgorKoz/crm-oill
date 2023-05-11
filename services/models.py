from django.db import models


class Service(models.Model):
    name = models.CharField('Услуга', max_length=255)
    count = models.PositiveSmallIntegerField('Количество')
    price = models.CharField('Стоимость', max_length=64)

    def __str__(self):
        return f'{self.name} Количество: {self.count} Стоимость: {self.price}'

    class Meta:
        verbose_name = 'Услуги'
