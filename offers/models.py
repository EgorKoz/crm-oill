from django.db import models
from contracts.models import Contract
from django.contrib.auth.models import User


STATUS = (
    ('a', 'Активно'),
    ('s', 'Приостановлено'),
    ('c', 'Закрыто'),
)


class Offer(models.Model):
    contract = models.OneToOneField(
        Contract,
        on_delete=models.PROTECT,
        related_name='offer'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
    created_on = models.DateTimeField('Дата создания', auto_now_add=True)
    send_on = models.DateField('Отправлено клиенту', blank=True,
                               null=True)
    status = models.CharField('Статус', max_length=3, choices=STATUS,
                              default='a')

    class Meta:
        ordering = ['-created_on', ]

    def __str__(self):
        return self.contract.name
