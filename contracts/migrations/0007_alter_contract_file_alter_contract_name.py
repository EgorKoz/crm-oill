# Generated by Django 4.2 on 2023-04-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_alter_contract_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='file',
            field=models.FileField(blank=True, default='', upload_to='contracts/', verbose_name='Договор'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Название'),
        ),
    ]
