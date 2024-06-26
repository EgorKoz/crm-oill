# Generated by Django 4.2 on 2023-04-28 17:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_alter_service_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agents', '0009_alter_org_web_site'),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='creted_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='file',
            field=models.FileField(blank=True, default='', upload_to='', verbose_name='Договор'),
        ),
        migrations.AddField(
            model_name='contract',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agents.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='send_on',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Отправлено клиенту'),
        ),
        migrations.AddField(
            model_name='contract',
            name='services',
            field=models.ManyToManyField(to='services.service'),
        ),
    ]
