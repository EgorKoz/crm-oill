# Generated by Django 4.2 on 2023-04-27 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_name'),
        ('applications', '0004_alter_application_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='services',
        ),
        migrations.AddField(
            model_name='application',
            name='services',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='services.service'),
            preserve_default=False,
        ),
    ]