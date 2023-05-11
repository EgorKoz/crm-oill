# Generated by Django 4.2 on 2023-04-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0010_alter_application_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='priority',
            field=models.CharField(blank=True, choices=[('l', 'Низкий'), ('m', 'Средний'), ('h', 'Высокий')], default='l', max_length=3, verbose_name='Приоритет'),
        ),
    ]
