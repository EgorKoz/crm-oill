# Generated by Django 4.2 on 2023-04-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0008_alter_profile_address_alter_profile_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='web_site',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Web-сайт'),
        ),
    ]
