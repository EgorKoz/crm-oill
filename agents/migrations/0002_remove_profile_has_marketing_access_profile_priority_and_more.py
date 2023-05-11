# Generated by Django 4.2 on 2023-04-23 11:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='has_marketing_access',
        ),
        migrations.AddField(
            model_name='profile',
            name='priority',
            field=models.CharField(blank=True, choices=[('l', 'Низкий'), ('m', 'Средний'), ('h', 'Высокий')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='org',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
