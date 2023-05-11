from django.db import models
from agents.models import Profile
from services.models import Service
from django.contrib.auth.models import User


class Contract(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='contract'
    )
    name = models.CharField('Название договора', max_length=64)

    file = models.FileField('Договор', blank=True, default='',
                            upload_to='')
    services = models.ManyToManyField(
        Service,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
    created_on = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name
