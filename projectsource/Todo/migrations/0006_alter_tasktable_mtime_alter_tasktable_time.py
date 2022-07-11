# Generated by Django 4.0.6 on 2022-07-10 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0005_tasktable_mtime_alter_tasktable_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktable',
            name='mtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tasktable',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
