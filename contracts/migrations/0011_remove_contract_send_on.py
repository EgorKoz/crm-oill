# Generated by Django 4.2 on 2023-05-01 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0010_alter_contract_send_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='send_on',
        ),
    ]
