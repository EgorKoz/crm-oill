# Generated by Django 4.2 on 2023-04-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0005_alter_profile_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Строение'),
        ),
    ]
