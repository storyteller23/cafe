# Generated by Django 3.2.13 on 2022-12-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_auto_20221221_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='server',
        ),
        migrations.AddField(
            model_name='position',
            name='server',
            field=models.BooleanField(default=True, verbose_name='Обслуживает клиентов'),
        ),
    ]
