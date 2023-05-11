# Generated by Django 4.2 on 2023-04-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0007_alter_profile_address_alter_profile_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(''), related_name='adress_users', to='agents.address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(''), related_name='user_org', to='agents.org'),
        ),
    ]
