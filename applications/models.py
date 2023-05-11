from django.db import models
from appeal.models import Appeal

PRIORITIES = (
    ('l', 'Низкий'),
    ('m', 'Средний'),
    ('h', 'Высокий'),
)
STATUS = (
    ('n', 'Не согласована'),
    ('s', 'Согласована'),
    ('k', 'У клиента'),
    ('c', 'Закрыта'),
)


class Application(models.Model):
    appeal = models.ForeignKey(
        Appeal,
        on_delete=models.PROTECT,
        related_name='app',
    )
    priority = models.CharField('Приоритет', max_length=3, choices=PRIORITIES,
                                default='l')
    created_on = models.DateTimeField('Дата создания', auto_now_add=True)
    status = models.CharField('Статус', max_length=3, choices=STATUS,
                              default='n')
    send_on = models.DateField('Отправлено клиенту', blank=True,
                               null=True)

    class Meta:
        ordering = ['-created_on', ]

    def __str__(self):
        return f'{self.appeal.get_topic_display()}, {self.get_status_display()}'
