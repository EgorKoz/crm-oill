# Generated by Django 4.2 on 2023-04-26 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appeal', '0007_remove_appeal_client_appeal_client'),
        ('services', '0001_initial'),
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='appeal',
            field=models.ForeignKey(blank=True, default=1, on_delete=models.SET(''), to='appeal.appeal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='priority',
            field=models.CharField(blank=True, choices=[('l', 'Низкий'), ('m', 'Средний'), ('h', 'Высокий')], default='', max_length=3, verbose_name='Приоритет'),
        ),
        migrations.AddField(
            model_name='application',
            name='services',
            field=models.ManyToManyField(to='services.service'),
        ),
    ]
