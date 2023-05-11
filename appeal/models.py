from django.db import models
from django.contrib.auth.models import User
from contracts.models import Contract
from agents.models import Profile
from datetime import date
from django.utils import timezone

TIME_ZONE = timezone.get_default_timezone()

TOPICS = (
    (None, ''),
    ('cd', 'Заключение договора'),
    ('cs', 'Изменение параметра услуг'),
    ('ud', 'Корректировка договора'),
    ('dd', 'Расторжение договора'),
)
CHANNEL = (
    (None, ''),
    ('e', 'Email'),
    ('p', 'Телефон'),
    ('m', 'Мессенджер'),
)
STATUS = (
    ('r', 'Обработано'),
    ('n', 'Не обработано'),
)


class Appeal(models.Model):
    client = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        related_name='appeal',
    )
    name = models.CharField('Название', max_length=64, blank=True, default='')
    topic = models.CharField('Тема', max_length=3, choices=TOPICS)
    contract = models.ForeignKey(
        Contract,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
    created_on = models.DateTimeField('Дата создания', auto_now_add=True)
    closed_on = models.DateField('Срок обработки', blank=True, default=date.today)
    channel = models.CharField('Канал поступления', max_length=3, choices=CHANNEL)
    comment = models.TextField('Комментарий', blank=True, default='')
    status = models.CharField('Статус', max_length=3, choices=STATUS, default='n')

    class Meta:
        ordering = ['-created_on', ]

    def __str__(self):
        output = (
            f'{self.created_on.astimezone(TIME_ZONE).strftime("%d.%m.%Y %H:%M")},'
            f' {self.get_channel_display()}')

        return output

    def get_services(self):
        return self.contract.services
